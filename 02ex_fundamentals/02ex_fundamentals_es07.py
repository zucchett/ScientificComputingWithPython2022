"""7. Decorators
Write a decorator named hello that makes every wrapped function print “Hello World!” each time the function is called.
The wrapped function should look like:
@hello
def square(x):
    return x*x
"""


def decorator(func):
    def wrapper(*args, **kw):
        func()
        # print(f'{func}')
    return wrapper


@decorator
def hello():
    print("Hello World!")


hello()
