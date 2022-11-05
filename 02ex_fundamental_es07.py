def hello(func):
    def wrapper(x):
        print("Hello World")
        func(x)  
    return wrapper
@hello
def square(x):
    print(x*x)
square(56)