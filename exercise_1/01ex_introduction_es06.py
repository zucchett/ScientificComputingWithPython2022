x = input("Enter first Number : ")
y = input("Enter second Number: ")
try:
    add = float(x) + float(y)
    print("The addition of the numbers are: %2.3f" % add)
except ValueError:
    print("Please enter the variables as int or float!!!")
