# 7. Decorators

def hello(func):
    def wrapper(*args):
        print('Hello World!')
        return (func(*args))
    return wrapper

@hello
def square(x):
    return x*x

@hello
def somef():
    return 9

square(21)
somef()