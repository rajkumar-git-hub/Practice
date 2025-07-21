def outer():
    print("Outer function started!")
    
    def inner():
        print("Inner function")

outer()
inner() #Type error

#How to invoke -inner function from outer function