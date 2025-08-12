import requests,json,csv
api_url='https://jsonplaceholder.typicode.com/users'
res=requests.get(api_url)

users=list(res.json())

fp1=open('user.json','w')

json.dump(users,fp1)
print("New File Is Created...!")

fp2=open('user.csv','w')

new_file=csv.writer(fp2)
new_file.writerows(users)
print("New File For CSV Is Created")