# Casting

a = input("Enter the first variable:")
b = input("Enter the second variable:")

try:
    a = float(a)
    b = float(b)
    print('Sum of 2 variables is :', a + b)

except:
    print('Please enter a valid number!')
