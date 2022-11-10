# 7. Decorators
# Write a decorator named hello that makes every wrapped
# function print “Hello World!” each time the function is called.

def hello(f):
    def wrapper(x):
        print("Hello World!")
        return f(x)

    return wrapper


@hello
def square(x):
    return x * x


x = 4
result = square(x)
print("Square of " + str(x), " is " + str(result))
