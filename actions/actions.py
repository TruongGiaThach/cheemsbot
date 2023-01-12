import difflib
import random
import re
import sqlite3
import string
import time
from datetime import datetime
from multiprocessing import connection
from sqlite3 import Error
from typing import Any, Dict, List, Text

import dateparser
from fuzzywuzzy import process
from rasa_sdk import Action, FormValidationAction, Tracker, ValidationAction
from rasa_sdk.events import AllSlotsReset, EventType, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

# import actions.psql as db
import actions.graphql_client as db

def time_extract(sentence):
    time = dateparser.parse(sentence, languages = ['vi'], region = 'vi', locales = ['vi'])
    return time

class ResetSlots(Action):
    def name(self) -> Text:
        return 'action_reset_slot'

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict
    ) -> List[EventType]:
        if tracker.get_slot('name') != None and tracker.get_slot('time') != None and tracker.get_slot('support') != None:
            AllSlotsReset()
        return []

# class DatLich(Action):
#     def name(self) -> Text:
#         return 'action_dat_lich'

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict
#     ) -> List[EventType]:
#         pass
#         return []
class GetInfoStore(Action):
    def name(self) -> Text:
        return "action_ask_info_store"

    def response_message(self, latest_message):

        list_category = db.get_info_store()
        print(list_category)
        if list_category == '0' or len(list_category) == 0:
            return "Cửa hàng hiện tại chưa có loại sản phẩm phục vụ !."
        else:
           
            message = "Các sản phẩm của cửa hàng hiện tại gồm \n "  
            for item in list_category:
                message += '* ' + item["name"] + ' \n '
            return message

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        latest_message = (tracker.latest_message)['text']
        message = self.response_message(latest_message)

        dispatcher.utter_message(text=message)
        return []

class CollectProductByProducCate(Action):
    def name(self) -> Text:
        return "collect_product_by_product_cate"

    def format_text(self,list_,cate):
        res = {
            "type" : "template",
            "payload":{
                "template_type": "generic",
                "elements":[

                ]
            }
        }
        for item in list_:
            image_url = ""
            if item["medias"] == []:
                image_url = "https://media.sproutsocial.com/uploads/2017/02/10x-featured-social-media-image-size.png"
            else: image_url = item["medias"][0]["filePath"]
            obj = {
                "title": item["name"],
                "subtitle": "sub",
                "image_url": image_url,
                "buttons": [{
                    "title": "Xem chi tiết",
                    "url": "https://cheems-angular-web.vercel.app/product-list/product/" + item["id"],
                    "type": "web_url"
                },
                {
                    "title": "Xem sản phẩm cùng loại",
                    "type": "web_url",
                    "url": "https://cheems-angular-web.vercel.app/product-list/" + cate,

                }
                # {
                #     "title": "Xem sản phẩm cùng loại",
                #     "type": "postback",
                #     "payload": "/affirm"
                # }
                ]
            }
            res["payload"]["elements"].append(obj)
        return res

    def response_message(self, latest_message, _cate = None):
        if  not _cate:
            return "Cửa hàng hiện tại chưa có loại sản phẩm phục vụ!", None
        products = db.get_info_from_cate(_cate)
        if products == None :
            return "Cửa hàng hiện tại chưa có loại sản phẩm phục vụ!", None
        else:
            # str_products = self.format_text(products)
            # message = "Các sản phẩm của cửa hàng thể loại " + _cate + "\n" + str_products + "---" 
            message = "Các sản phẩm của cửa hàng thể loại " + _cate + "\n" 
            res = self.format_text(products,_cate)
            return message, res

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        latest_message = (tracker.latest_message)['text']
        category_value = tracker.get_slot("productCategory")
        if not category_value:
            dispatcher.utter_message(text="không cate",attachment=None)
        message, res = self.response_message(latest_message, category_value)

        dispatcher.utter_message(text=message, attachment=res)
        return []

class QueryOrderUpdate(Action):

    def name(self) -> Text:
        return "place_confirmed_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = dbQueryMethods.create_connection("chatb_db/sqlTemp.db")
        
        #get user_id from tracker
        user_id = tracker.current_state()['sender_id']
        print(f"user-id:{user_id}")

        #initiate query to update order table
        current_order_id = dbQueryMethods.order_update_insert_query(conn, user_id)
        #display order status to user
        return_text_for_order_update = dbQueryMethods.order_status_check(conn, current_order_id)
        print(return_text_for_order_update)
        dispatcher.utter_message(text=str(return_text_for_order_update))

class QueryOrderStatus(Action):

    def name(self) -> Text:
        return "check_confirmed_order_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = dbQueryMethods.create_connection("chatb_db/sqlTemp.db")

        var1 = QueryOrderUpdate.current_order_id
        print(f"var1:{var1}")
        #display order status to user
        return_text_for_order_update = dbQueryMethods.order_status_check(conn, var1)
        print(return_text_for_order_update)
        dispatcher.utter_message(text=str(return_text_for_order_update))

class collectProductInfo(Action):

    def name(self) -> Text:
        return "collect_product_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = dbQueryMethods.create_connection("chatb_db/sqlTemp.db")
        user_id = tracker.current_state()['sender_id']
        print(f"user-id:{user_id}")

        # get matching entries for category value
        category_value = tracker.get_slot("productCategory")
        #make sure we don't pass None to our fuzzy matcher
        if category_value == None:
            category_value = " "
        print(f"category_slot_1:{category_value}")  #for debugging
        category_name = "ProductCategory"

        category_value = dbQueryMethods.get_closest_value(conn, category_name, category_value)[0]
        print(f"category_fuzzy_slot_2:{category_value}")

        query_result_category = dbQueryMethods.select_by_category(conn, category_value)

        # get matching entries for role value
        role_value = tracker.get_slot("products")
        #make sure we don't pass None to our fuzzy matcher
        if role_value == None:
            role_value = " "
        role_name = "ProductRoles"
        print(f"role_slot_1:{role_value}")  #for debugging
        
        role_value = dbQueryMethods.get_closest_value(conn, role_name, role_value)[0]
        print(f"role_fuzzy_slot_2:{role_value}")

        query_result_roles = dbQueryMethods.select_by_slots(conn, role_value)

        # apology for not being able to find a match
        apology = "I'm sorry, I couldn't find exactly what you wanted, but you might like this."

        # intersection of two queries
        query_result_overlap = list(set(query_result_category) & set(query_result_roles))
        

        # return info for both, or category match or role match or nothing
        if len(query_result_overlap)>0:
            return_text_for_general_query = dbQueryMethods.rows_as_info_text(query_result_overlap)
            print(f"query_result_overlap:{query_result_overlap}")
        elif len(list(query_result_category))>0:
            return_text_for_general_query = apology + dbQueryMethods.rows_as_info_text(query_result_category)
            print(f"query_result_category:{query_result_category}")
        elif len(list(query_result_roles))>0:
            return_text_for_general_query = apology + dbQueryMethods.rows_as_info_text(query_result_roles)
            print(f"query_result_roles:{query_result_roles}")
        else:
            return_text_for_general_query = dbQueryMethods.rows_as_info_text(query_result_overlap)
        
        # look at intersect between two arrays
        # if empty && union is not
        # randomly select one item from list
        # otherwise get query results from one of the two arrays

        print(return_text_for_general_query)
        dispatcher.utter_message(text=str(return_text_for_general_query))

class dbQueryMethods:
    def create_connection(sqlTemp):
        """ create a database connection to the SQLite database      
            """
        conn = None
        try:
            conn = sqlite3.connect(sqlTemp)
            print(dbQueryMethods.create_connection)
        except Error as e:
            print(e)
        return conn
    
    def get_closest_value(conn, slot_name, slot_value):
        """ Given a database column & text input, find the closest 
        match for the input in the column.
        """
        # get a list of all distinct values from our target column
        fuzzy_match_cur = conn.cursor()
        fuzzy_match_cur.execute(f"""SELECT DISTINCT {slot_name} 
                                FROM Product""")
        column_values = fuzzy_match_cur.fetchall()

        top_match = process.extractOne(slot_value, column_values)

        conn.commit()

        return(top_match[0])

    def select_by_category(conn, slot_value):
        """
        Given a database column & text input, find the 
        closest match for product category.
        """
        cur = conn.cursor()
        cur.execute(f"""SELECT ProductName 
            FROM Product
            WHERE ProductCategory = '{slot_value}'""")

        rows = cur.fetchall()
        conn.commit()

        return(rows)
    
    def select_by_slots(conn,slot_value):
            """
            Query all rows in the tasks table
            :param conn: the Connection object
            :return:
            """
            cur = conn.cursor()
            cur.execute(f"""SELECT ProductName 
                FROM Product
                WHERE ProductRoles = '{slot_value}'""")

            # return an array
            rows = cur.fetchall()
            conn.commit()
            
            return(rows)

    def order_update_insert_query(conn, user_id):
        """ Update the Order table with 
        randomly/uniquely generated user_id and order_id"""

        cur = conn.cursor()
        current_date = time.strftime("%Y-%m-%d")
        chars =  string.ascii_lowercase + string.digits
        order_new_id = ''.join(random.choice(chars) for _ in range(10))
        # insert a new row of data
        cur.execute(f"INSERT INTO `Order`(OrderNumber, CustomerId, OrderDate) VALUES('{order_new_id}','{user_id}','{current_date}')")
        return order_new_id

    def order_status_check(conn, order_new_id):

        cur = conn.cursor() 
        # display the last inserted row
        cur.execute(f"""SELECT * FROM `Order`
         WHERE OrderNumber = '{order_new_id}'""")
        # return an array
        rows = cur.fetchall()
        conn.commit()
        rows = list(rows)
        for row in range(len(rows)):
            return(f"Your order number is {(rows[row][1])} and your order date is {(rows[row][3])}")

    def rows_as_info_text(rows):    
        
            if len(list(rows)) < 1:     #if cursor is carrying Empty Val from query
                return("There are no products matching your query in the database")
            
            else:
                for row in random.sample(rows, 1):
                    return f"we have {row[0]} in stock."

            
