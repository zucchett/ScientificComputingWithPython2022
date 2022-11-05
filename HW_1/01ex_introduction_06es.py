# Entering the variables
x = input("enter a int/float/str variable: ")
y = input("enter the second int/float/str variable: ")

try:
    addition = float(x) + float(y)
    print("The 2 variables can be added. The sum is: ", addition)  # this is not printing because there is an error
except:
    print("The variables " + x + "," + y + " cannot be added.")
    if x.isalpha() and y.isalpha():  # checks whether the string has alphabets or not
        new_string = x + y
        print("Sum of the 2 strings is " + new_string + ".")
finally:
    print("operation finished")
