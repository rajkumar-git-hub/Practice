
import csv

fp=open('emp.csv','r')

d=csv.reader(fp)

print(type(d))

for i in d:
    print(i)

fp.close()





