# 6. Nested functions
# Write two functions: one that returns the square of a number, and one that 
# returns its cube.
# Then, write a third function that returns the number raised to the 6th power, 
# using only the two previous functions.

def square(x):
    return x*x

def cube(x):
    return x*x*x

def sixth_power(x):
    return square(x)*cube(x)*int(cube(x)/square(x))
    #return square(x)*cube(x)*x

x = 4
print("Result of function: "+str(sixth_power(x)))
print("Result of calculation: "+str(x**6))