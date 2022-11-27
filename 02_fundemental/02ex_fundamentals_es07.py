def hello(func):
    def wrapper(a):
        print("Hello World")
        print(func(a))
    return wrapper

@hello
def square(x):
    return x*x

square(3)

def hello(func):
    def wrapper(a):
         
        print("Hello World")
        returned_value = func(a)
        return returned_value
         
    return wrapper
 
 
# adding decorator to the function
@hello
def square(x):
    print("Inside the function")
    return x*x
 
a, b = 1, 2
square(b)

