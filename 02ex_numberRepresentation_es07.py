def hello(Myfunc):
    def wrapper(x):
        print("Hello World!")
        Myfunc(x)
        print(Myfunc(x))
    return wrapper

@hello
def square(x):
    return x*x

print(square(3))

