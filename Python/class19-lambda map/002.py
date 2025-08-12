enames=['arisu','bonil','caren','diren']

def change_name(n):
    return n.upper()
m=map(change_name,enames)
print(list(m))

# method-2

upp=list(map(lambda x:x.upper(),enames))
print(upp)