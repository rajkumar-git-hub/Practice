import csv
fp=open('emp.csv')

emp_data=list(csv.reader(fp))
employees = emp_data[1:]   #We are using 

for emp in employees:
    print(emp)

fp.close()