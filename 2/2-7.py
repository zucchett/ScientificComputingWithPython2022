def hello(func):
    def wrapper(*args, **kwargs):
        print('Hello World')
        a = func(*args, **kwargs)
        return a
    return wrapper


@hello
def square(x):
    return x*x

square(2)