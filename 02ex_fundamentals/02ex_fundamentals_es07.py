
# 7. Decorators

# Write a decorator named hello that makes every wrapped
# function print “Hello World!” each time the function is called.

# -------------------------------------- Code Begin-------------------------------------


def hello(func):
    def wrapper(x):
        print("Hello World!")
    return wrapper

@hello
def square(x):
    return x*x

square(25)

# -------------------------------------- Code Begin-------------------------------------
