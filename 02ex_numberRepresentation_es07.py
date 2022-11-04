def hello(Myfunc):
    def wrapper(x):
        print("Hello World!")
        Myfunc(x)
        print(Myfunc(x))
    return wrapper

@hello
def square(x):
    return x*x

print('calling square(3) function using decorator: ')
square(3)
