def hello(myfunction):
    def wrapper(x):
        print("Hello World")
        myfunction(x)  
    return wrapper
@hello
def square(x):
    print(x*x)
square(40)