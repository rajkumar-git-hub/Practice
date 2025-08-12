import json

e=[
    {"sid":1001, "sname": "Zunir", " pass": True , "data" : " None"},
    {"sid":1002, "sname": "Ymir", " pass": False , "data" : " None"},
    {"sid":1003, "sname": "Xunex", " pass": False , "data" : " None"}
]


student=json.dumps(e)

print(student)