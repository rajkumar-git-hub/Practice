def add(a,b):
    return a+b

r1=add (10,20)
print(r1)

sub = lambda a,b:a-b  #we use lambda expresssion instead of def keyword, return call

print(type(sub))

r2= sub(20,10)

print (r2)