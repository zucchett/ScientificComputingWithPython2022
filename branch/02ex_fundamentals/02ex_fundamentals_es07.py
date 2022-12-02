#ex_07 
#Write a decorator named hello that makes every wrapped function print “Hello World!” each time the function is called.

def hello(func): 
    def wrappedfunc(x):
        print("Hello World!")
        squaring = func(x)
        print(squaring)
        #print("Hello World!")
    return wrappedfunc

@hello    
def square(x): 
    return x*x

z = float(input("Enter a number: "))    

square(z)
