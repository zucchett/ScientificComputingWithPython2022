# 6. Casting

# Write a program that:

# reads from command line two variables, that can be either int, float, or str.
# use the try/except expressions to perform the addition of these two variables, only if possible
# and print the result without making the code crash for all the int/float/str input combinations.

v1 = input("The first variable v1 is: ")
v2 = input("The second variable v2 is: ")

try:
    sum = float(v1) + float(v2)
    print("The sum of the two variables is ", sum)
except:
    if v1.isalpha() and v2.isalpha() :
        print("The sum can not be computed because both v1 and v2 are strings: " + v1 + ", " + v2)
    elif v1.isalpha() :
        print("The sum can not be computed because v1 is a string: ", v1)
    else :
        print("The sum can not be computed because v2 is a string: ", v2)