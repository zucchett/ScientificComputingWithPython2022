def hello(func):
    def wrapper(x):
        print("Hello World!")
        returned_value = func(x)
        return returned_value
    return wrapper
        
@hello
def square(x):
    return x*x

print(square(7))
print(square(5))
print(square(2))
