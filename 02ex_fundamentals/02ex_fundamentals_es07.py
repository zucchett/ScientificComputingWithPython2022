def hello(func): 
    def wrapper(x):
        print("Hello World!")
        squaring = func(x)
        print(squaring)
        #print("Hello World!")
    return wrapper

@hello    
def square(x): 
    return x*x

z = float(input("Enter a number: "))    

square(z)

print()
