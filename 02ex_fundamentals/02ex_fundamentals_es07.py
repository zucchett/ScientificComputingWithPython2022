def hello(function):
    def wrapper(x):
        print("Hello World!")
        function(x)
    return wrapper

@hello
def square(x):
    print(x*x)
    
square(2)