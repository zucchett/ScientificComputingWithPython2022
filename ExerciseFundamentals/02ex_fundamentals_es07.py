"""
7. Decorators
Write a decorator named hello that makes every wrapped function print “Hello World!” each time the function is called.
The wrapped function should look like:
@hello
def square(x):
    return x*x
"""


def hello(func):
    def wrapper(X):
        print("Hello World!")
        return func(X)

    return wrapper


@hello
def square(X):
    return X * X


x = 2
result = square(x)
print("Square of " + str(x), " = " + str(result))
