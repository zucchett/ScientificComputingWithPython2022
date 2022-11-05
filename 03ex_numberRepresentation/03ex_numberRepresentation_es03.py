# 3. Underflow and overflow

# Write a program to determine the underflow and overflow
# limits (within a factor of 2) for floating point numbers on your computer.

# Hint: define two variables initialized to 1, and halve/double them for a sufficient amount
# of times to exceed the under/over-flow limits.


# -------------------------------------- Code Begin-------------------------------------

import math

underflow = 1.0
overflow = 1.0

while True:
    overflow *=2
    if math.isinf(overflow *2):
        break
while True:
    underflow /=2
    if underflow/2 == 0:
        break
print('Overflow limit : ', overflow)
print('Underflow limit : ', underflow)

# -------------------------------------- Code End  -------------------------------------
