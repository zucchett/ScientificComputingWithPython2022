def hello(func):
    def wrapper(x):
        print("Hello World")
        result = func(x)
        return result
    return wrapper

@hello
def square(x):
    return x*x

x = int(input("Insert a number: "))
print(square(x))