def outer():
    print("Outer function started!")
    
    def inner():
        print("Inner function")
    return inner  #(returning inner function reference)
    
inner=outer()

print(type(inner))
inner()
inner()
outer()