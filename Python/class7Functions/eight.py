#variable length arguments
def info(a,*b):
    print("a:",a,"-","b:",b)

info(10,20)
info(10,20,30)
info(10,20,30,40)

#TyepeError: info(a,b) takes 2 args but provided  3 
#so we use info(a,*b)