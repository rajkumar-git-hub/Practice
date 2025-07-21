def outer():
    print("Outer function started!")
    
    def inner():
        print("Inner function")

    inner()
    inner()

outer()