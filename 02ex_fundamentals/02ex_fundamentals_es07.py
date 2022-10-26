def hello(func):
    def wrapper():
        print("Hello World!")
    return wrapper

@hello
def square(x):
    return x*x

