import csv,json

fp1=open('user_data.json','r')
fp2=open('user.json','w')
fp3=open('user.csv','w',newline="")  #by default it takes one empty line. So, we use this newline="" -- it means null

user_data=json.load(fp1)
u=user_data['users']

json_users=[]
csv_users=[]


for user in u:
    json_users.append({'userid':user['id'],'fname':user['firstName'],'age':user['age'],'gender':user['gender']})
    csv_users.append((user['id'], user['firstName'], user['age'], user['gender']))

#print(json_users)
#print(csv_users)


data=json.dump(json_users,fp2)
print('New JSON file is created.')


c=csv.writer(fp3)
c.writerow(['userid','fname','age','gender'])
c.writerows(csv_users)

print("New CSV file created")

fp1.close()
fp2.close()
fp3.close()
