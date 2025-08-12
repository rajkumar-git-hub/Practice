import json

e='''
[
    {"sid":1001, "sname": "Zunir", " pass": true , "data" : " null"},
    {"sid":1002, "sname": "Ymir", " pass": false , "data" : " null"},
    {"sid":1003, "sname": "Xunex", " pass": true , "data" : " null"}
]
'''

student=json.loads(e)

print(student)