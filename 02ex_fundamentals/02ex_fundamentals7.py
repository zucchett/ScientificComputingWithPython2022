# 7. Decorators

# Write a decorator named hello that makes every wrapped function print “Hello World!” 
# each time the function is called.

# The wrapped function should look like:

# @hello
x = int(input("Enter A number :"))


def hello(func):
    def wrapper(x):
        print("Hello World!")
        print(func(x))
    return wrapper

@hello
def square(x):
    return x*x

square(x)