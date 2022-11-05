def hello(function1):
    def wrapper(x):
        print("Hello World")
        function1(x)  
    return wrapper
@hello
def square(x):
    print(x*x)
square(12)