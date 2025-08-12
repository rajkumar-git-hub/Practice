'''USAGE:fetch all users
API URL:https://jsonplaceholder.typicode.com/users
Method:GET
Required Fields: None
Access Type:P
'''

import requests
api_url='https://jsonplaceholder.typicode.com/users'
response=requests.get(api_url)

print(response)
