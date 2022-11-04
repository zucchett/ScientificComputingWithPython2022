def square(x):
    return x**2

def cube(x):
    return x**3
    
y = float(input("Enter a number: "))

print("The square of your number is: ", square(y))
print("The cube of your number is: ", cube(y)) 
print("Your number elevated to the sixth power is: ", cube(square(y)))   
print()
