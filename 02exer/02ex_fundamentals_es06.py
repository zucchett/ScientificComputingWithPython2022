#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
from pyrsistent import s

#square function
def square(x):
    s = x**2
    return s

#cube function
def cube(x):
    c = x**3
    return c
x = float(input("Insert a number: "))

#print square(x) and cube(x)
print("The square of "+str(x)+" is: "+str(square(x)))
print("The cube of "+str(x)+" is: "+str(cube(x)))

#6-th power function
def six(x):
    d = square(x)**3
    return d
    
#print(six(x))
print("The 6-th power of "+str(x)+" is: "+str(six(x)))
