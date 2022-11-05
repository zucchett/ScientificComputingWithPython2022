# 6. Nested functions

# Write two functions: one that returns the square
# of a number, and one that returns its cube.

# Then, write a third function that returns the number 
# raised to the 6th power, using only the two previous functions.

def square(n):
    return n*n

def cube(n):
    return pow(n,3)

def six_pow(n):
    return square(cube(n))

N = int(input("Insert the number N: "))

print("N to the 6-th power is: " + str(six_pow(N)))

print("Exercise done!")