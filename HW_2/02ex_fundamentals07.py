# Decorator
def hello(s):
    def wrapper():
        print("hello world")

    return wrapper


@hello
def say_hi():
    print("working")


say_hi()
