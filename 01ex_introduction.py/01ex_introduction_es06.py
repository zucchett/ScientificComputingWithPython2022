a = input("Enter first number")
b = input("Enter second number")

try:   
    a=float(a)
    b=float(b)
    print("Sum of the numbers: ",a+b)

except:
    print("Please enter valid number")