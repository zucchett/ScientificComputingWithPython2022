def hello(func):
    def wrapper(*args):
        print("hello world!")
        return func(*args)
    return wrapper

@hello
def square(x):
    return x*x

print(square(2))
