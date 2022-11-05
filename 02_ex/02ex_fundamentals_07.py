def hello(func):
    def wrapper(arg):
        print("Hello World!")
        return func(arg)
    return wrapper
@hello
def square(x):
    return x * x

print(square(3))
print(square(7))
print(square(4))