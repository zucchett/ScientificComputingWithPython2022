def helloworld(fun): 
    def h(x):
        print("Hello,World!")
        d = fun(x)
        print(d)
        #print("Hello,World!")
    return h
@helloworld    
def s(x): 
    return x*x
f = float(input("Enter the number: "))    
s(f)