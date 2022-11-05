# 7. Decorators

# Write a decorator named hello that makes
# every wrapped function print “Hello World!”
# each time the function is called.

# The wrapped function should look like:

# @hello
# def square(x):
    # return x*x

def hello(func):
    def wrapper(x):
        print("Hello World!")
        func(x)
    return wrapper

@hello
def square(x):
    y = x*x
    print("The square of " + str(x) + " is "+ str(y))

n = 10
print("By calling the function, it displays: ")
square(n)
