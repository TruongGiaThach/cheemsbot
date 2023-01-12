from requests.auth import HTTPBasicAuth
from python_graphql_client import GraphqlClient
import asyncio


# Create the query string and variables required for the request.

def create_connection():
    client = None
    try:
        auth = HTTPBasicAuth('19522339@gm.uit.edu.vn', '0981097144')
        client = GraphqlClient(endpoint="https://cheems-store.onrender.com/graphql/", auth=auth)
    except (Exception) as e:
        print(e)
    return client

def get_info_store():
    data = []
    client = create_connection()
    query = ('''
        query Categories($_filter: CategoriesFilterInput!){
            categories(input: $_filter) {
                items {
                    id,
                    name
                }
            } 
        
        }
    ''')
    variables = {
        "_filter": {
            # "names":[
            #   "Laptop"
            # ]
        }
    }
    # Synchronous request
    data = client.execute(query=query, variables=variables)
    print(data) 
    if data != []:
        data = data['data']['categories']['items']
    return data

def get_cate_id_from_cate_name(_cate, client):
    data = []
    query = ('''
        query Categories($_filter: CategoriesFilterInput!){
            categories(input: $_filter) {
                items {
                    id
                }
            } 
        
        }
    ''')
    variables = {
        "_filter": {
            "names":[
              _cate
            ]
        }
    }
    # Synchronous request
    data = client.execute(query=query, variables=variables)
    print("sadsasdaas",data)
    if data != [] and  data['data']['categories']['items'] != []:
        data = data['data']['categories']['items'][0]['id']
    else: data = None
    return data

def get_info_from_cate(_cate):
    client = create_connection()
    _cate_id = get_cate_id_from_cate_name(_cate,client)
    if _cate_id == None:
        return None
    data = []
    query = ('''
        query($input: ProductTypesFilterInput) {
            productTypes(input: $input) {
                items {
                    id,
                    name,
                    description,
                    medias {
                        id,
                        filePath,
                        fileSize,
                        fileType
                    },
                    price,
                    warrantyPeriod
                }
            }
        }
    ''')
    variables = {
        "input": {
            "isDeleted": False,
            "categoriesIds": [
                _cate_id
            ]
	    }
    }
    # Synchronous request
    data = client.execute(query=query, variables=variables)

    # Asynchronous request
    # data = asyncio.run(client.execute_async(query=query, variables=variables))
    if data != []:
        data = data['data']['productTypes']['items']
    return data

 # => {'data': {'country': {'code': 'CA', 'name': 'Canada'}}}


# Asynchronous request
# import asyncio

# data = asyncio.run(client.execute_async(query=query, variables=variables))
# print(data)  # => {'data': {'country': {'code': 'CA', 'name': 'Canada'}}}