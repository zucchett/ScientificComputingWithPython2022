
# 6. Nested functions

# Write two functions: one that returns the square of a number, and one that returns its cube.

# Then, write a third function that returns the number raised t
# o the 6th power, using only the two previous functions.

# -------------------------------------- Code Begin-------------------------------------

square = lambda x :x*x
cube = lambda x : square(x)*x
sixth_power = lambda x : cube(square(x))


n = 2
print('The 6th power of {} is {}'.format(n,sixth_power(n)))

# -------------------------------------- Code End ---------------------------------------
