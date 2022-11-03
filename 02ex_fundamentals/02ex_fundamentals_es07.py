def hello(func):
    def wrapper(*args):
        print("hello world!")
        return func(*args)
    return wrapper

@hello
def square(x):
    return x*x
#@hello
#def cube(x):
#    return x**3

print(square(2))
#print(cube(2))
