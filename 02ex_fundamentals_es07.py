def Hello_world(func):
    def wrapper(x):
        print("Hello World")
        func(x)  
    return wrapper
@Hello_world
def squ(x):
    print(x*x)
squ(int(input("enter number: ")))