#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
# defining a decorator
#def func(string):
#    def wrapper():
#        print("Start")
#        print(string)
#        print("End")

    #return wrapper()

#x = func("Hello")
"""
def func(f):
    def wrapper():
        print("Start")
        f()
        print("End")

    return wrapper

@func #it is the same of func2 = func(func2); func is the name of the function that I want to run before 
def func2():
    print("I am func2")


@func #it is the same of func3 = func(func3)
def func3():
    print("I am func3")

#x = func(func3)


#x = func(func2)
#func3 = func(func3)
func3()
func2()
###########################################################
def func(f):
    def wrapper(x):
        print("Start")
        f(x)
        print("End")

    return wrapper

@func #it is the same of func2 = func(func2); func is the name of the function that I want to run before 
def func2(x):
    print(x)


@func #it is the same of func3 = func(func3)
def func3():
    print("I am func3")
#func3()
func2(5)
"""
##########################################
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