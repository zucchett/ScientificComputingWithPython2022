#ex_06 
# Write two functions: one that returns the square of a number, and one that returns its cube, and one that returns its sixth power.

def square(x):
    return x**2

def cube(x):
    return x**3

y = int(input("Enter a number: "))

print("The square of your number is: ", square(y))
print("The cube of your number is: ", cube(y)) 
print("Your number elevated to the sixth power is: ", cube(square(y)))   

