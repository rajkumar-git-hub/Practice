emp={
    'eid':101,
    'ename':'Rahul Gandhi',
    'esal':45000.45
}

#print(emp['loc'])           #KeyError.
print(emp.get('eid'))        #101
print(emp.get('loc'))        #None

# In Normally we use if the key is not there it shows Key error.
# In get() method if there is no key it won't show Key error . It shows None.
