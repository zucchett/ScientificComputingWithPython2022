# 4. Machine precision

# Similarly to the previous exercise, write a program to
# determine the machine precision for floating point numbers.

# Hint: define a new variable by adding an increasingly smaller
# value and check when the addition starts to have no effect on the number.

var1 = float(input("Insert a number for which computing the machine precision: "))
factor = 1

while var1 + factor != var1:
    print("Now factor is " + str(factor))
    factor = factor/2

print("The machine precision for var1 = " + str(var1) + " floating point number is " + str(2*factor))

# exercise done!