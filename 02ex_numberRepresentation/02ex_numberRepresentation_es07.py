def hello(func):
    def wrapper(x):
        print("Hello World!")
        func(x)
        print("Hello World!")
    return wrapper

@hello
def square(x):
    print(x * x)

square(2)
