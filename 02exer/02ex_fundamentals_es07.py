#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
# defining a decorator
def hello(f):
    def wrapper(x):
        f(x)
        print("Hello World")
        
    return wrapper
        

@hello
def square(x):
    print(x*x)
    return x*x

square(4)
square(6)