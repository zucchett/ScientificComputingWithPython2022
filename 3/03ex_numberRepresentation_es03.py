# 3. Underflow and overflow

# Write a program to determine the underflow and overflow limits 
# (within a factor of 2) for floating point numbers on your computer. 

# *Hint*: define two variables initialized to 1, and halve/double them 
# for a sufficient amount of times to exceed the under/over-flow limits.

from math import isinf

num_1 = 1.0
num_2 = 1.0
num_prev = 0

while not isinf(num_1):
    num_prev = num_1
    num_1 = num_1 * 2

print("Overflow limit by using 1.0: ", num_prev)

num_prev = 0
while num_2 != 0:
    num_prev = num_2
    num_2 = num_2 / 2

print("Underflow limit by using 1.0: ", num_prev)