def hello (func):
    def wrapper(x):
        f=func(x)
        print("Hello World!")
        return f
        
    return wrapper
@hello
def square(x):
    return x*x
print(square(5))