#7. Decorators
def hello2(func2):
    def wrapper2(x):
        print("Hello World!")
        return func2(x)
       
    return wrapper2

@hello2
def square(x):
    return x*x

print(square(2))