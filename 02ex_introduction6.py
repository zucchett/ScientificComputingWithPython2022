# 6. Nested functions
# Write two functions: one that returns the square of a number, and one that returns its cube.
# Then, write a third function that returns the number raised to the 6th power
# , using only the two previous functions

def sqr(nr):
  return nr**2
def cub(nr):
  return nr**3

def sixth(nr):
  return cub(sqr(nr))

print(sqr(2),cub(3),sixth(2))