
# we can convert json data to py data using loads.

import json
emp_json_str = ''' 
[
    {"eid":101, "ename":"Raj", "avail":true,"email":null,"location":null},
    {"eid":102, "ename":"spidey", "avail":false,"email":null,"location":null}
]
'''
employees=json.loads(emp_json_str)
print(employees)
