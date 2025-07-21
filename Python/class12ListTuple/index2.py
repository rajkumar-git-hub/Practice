enames=['Rahul','sonia','priyanka','modi','amit','Rahul']
print(enames.index('sonia')) #1
#print(enames.index('sharukh')) #valueError
print(enames.count("Rahul"))  #2

enames.append('Raj')
print(enames)

enames.extend(['lala','maxi'])
print(enames)

enames.sort()
print("After sorting  Ascending order")
print(enames)

enames.sort(reverse=True)
print("After sorting  Desending order")
print(enames)

enames.pop(2)
print(enames)

enames.remove('amit')
print(enames)

enames.clear()
print(enames)

