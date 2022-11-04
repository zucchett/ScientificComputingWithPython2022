def hello(func):
    def wrapper(x):
        print("Hello World")
        return func(x)
    return wrapper

#funzione originale con decoratore:
@hello
def square(x):
    return x*x

x=square(5)
print("Result of original function: ",x)