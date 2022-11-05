def hello(func):
    def wrap(x):
        print("Hello World!")
        return func(x)    
    return wrap

@hello
def square(x):
    return x*x

print(f"The square of 2 is {square(2)}")
