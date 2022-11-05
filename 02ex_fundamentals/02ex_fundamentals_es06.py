#6. Nested functions

Square = lambda x : x**2 #Square is a function that claculates the square of a number
Cube = lambda x : x**3 #Cube is a function that claculates the cube of a number
power6 = lambda x : Square(Cube(x)) #(x**2)** 3== x**6
x=3
print("The 6th power of x=%d is %d"%(x,power6(x)))
