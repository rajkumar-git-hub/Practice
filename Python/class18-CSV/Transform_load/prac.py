import json

fp1=open('user_data.json','r')

data=json.load(fp1)

u=data['users']

fp2=open('user.json','w')

new_user=[]

for i in data:
    new_user.append({'Userid':i[id], 'Name':i['firstName'], 'Age':['age']})

print(new_user)
