a = 9 
b = 77

def outerfun():
    print("\nThis is the outer function:")
    a = 20
    b = 90
    print(f"The value of a and b inside a function as enclosing function is: {a} , {b}")
    print("The addition of a and b is : " , a+b)
    print("The above printed value in from outer function")    
    def innerfunc():
        print("\nThis is the inner function")
        print("The addition of a and b is : " , a+b)   # the value of a and b is taken from outer function  
        print("Inner function completed!!")
        
    innerfunc()
    print("\nOuter function completed")
    
# driver code
print("driver code:")
print(f"The values of a and b in global scope is : {a} and  {b}" )
outerfun()
