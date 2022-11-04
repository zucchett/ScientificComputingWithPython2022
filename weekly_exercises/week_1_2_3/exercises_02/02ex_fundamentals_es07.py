#Zuccolo Giada, matr. 2055702
# EXE 7

def hello(func):
    def wrapper():
        print("Hi! I'm in wrapper")
        x = int(input("enter value: "))
        print(func(x))
        print("I'm going out of the wrapper..")
    return wrapper

@hello
def square(x):
    print("\tHello!")
    return "\tThe square of " + str(x) + " is = " + str(x * x)

square()