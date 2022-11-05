def hello(func):
    def wrapper(arg):
        print("Hello World!")
        return func(arg)
    return wrapper


@hello
def square(x):
    return x * x


print(square(5))
print(square(2))
print(square(3))
