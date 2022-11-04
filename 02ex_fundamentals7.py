x = int(input("Please write a number:"))

def hello(func):
    def wrapper(x):
        print("Hello world")
        print(func(x))
    return wrapper


@hello
def square(x):
    return x*x
square(x)