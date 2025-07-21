l1=[]
l2=list()
l3=[10,20,30,40,50]
l4=[10,10,10,10,20]
l5=[10,20.5,"RAJ",True,{10}]

print(type(l1))
print(type(l2))
print(type(l3))
print(type(l4))
print(type(l5))


print(l1)
print(l2)
print(l3)
print(l4)
print(l5)

print("AFTER APPLYING LIST METHODS")
l1.append(101)
l2.extend([101,202,303])
l3.remove(30)
l4.pop(4)
l5.reverse()

print(l1)
print(l2)
print(l3)
print(l4)
print(l5)