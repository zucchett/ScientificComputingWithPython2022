#7. Decorators

def hello(f):
    def wrapper(x):
        print(f(x))
        print("Hello world")
    return wrapper

@hello
def square(x):
    return x*x

x=5
square(x)
