import difflib
import re
from datetime import datetime
from typing import Any, Dict, List, Text

import dateparser
from rasa_sdk import Action, FormValidationAction, Tracker, ValidationAction
from rasa_sdk.events import AllSlotsReset, EventType, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

import psql as db

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

    def format_text(self,list_):
        s = ''
        for item in list_:
            s += item[0] +'\n'
        return s

    def response_message(self, latest_message):

        list_category = db.get_info_store()
        print(list_category)
        if list_category == '0' or len(list_category) == 0:
            return "Cửa hàng hiện tại chưa có loại sản phẩm phục vụ !."
        else:
            str_list_category = self.format_text(list_category)
            message = "Các sản phẩm của cửa hàng hiện tại gồm \n" + str_list_category + "---" 
            return message

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        latest_message = (tracker.latest_message)['text']
        message = self.response_message(latest_message)

        dispatcher.utter_message(text=message)
        return []