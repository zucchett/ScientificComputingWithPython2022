def hello(func):
    def wrapper(n):
        print('Hello World!')
        func(n)
    return wrapper

@hello
def square(x):
    return x*x

square(2)