#7. Decorators

def hello(func): 
        print("Hello!")
    

@hello
def square(x):
    return x*x