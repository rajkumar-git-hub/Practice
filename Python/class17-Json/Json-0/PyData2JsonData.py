
# we can convert jsond data to py data using loads.

import json
emp_json_str =  [
                {'eid':101, 'ename':'Raj', 'avail':True,'email':None,'location':None},
                {'eid':102, 'ename':'spidey', 'avail':False,'email':None,'location':None}
                ]

employees=json.dumps(emp_json_str)
print(employees)
