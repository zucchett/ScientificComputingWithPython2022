def hello(func):
    def wrapper(x):
        print("Hello World!")
        returned_value = func(x)
        return returned_value
    return wrapper

@hello
def square(x):
    return x*x

print(square(1))
print(square(2))
print(square(3))