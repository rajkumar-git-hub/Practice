def find_max(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=a:
        return b
    else:
        return c
    
print(find_max(10,25,15))