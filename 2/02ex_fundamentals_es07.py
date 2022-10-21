# 7. Decorators
# Write a decorator named `hello` that makes every wrapped function print 
# “Hello World!” each time the function is called.
# The wrapped function should look like:
# ```python
# @hello
# def square(x):
#     return x*x
# ```

def hello(func):
    def wrapper(x):
        print("Hello World!")
        return func(x)
    return wrapper

@hello
def square(x):
    return x*x

x = 2
result = square(x)
print("Square of "+str(x)," = " +str(result))