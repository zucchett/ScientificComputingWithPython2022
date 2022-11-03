"""
3. Underflow and overflow

Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your
computer.

*Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed
the under/over-flow limits.
"""

import math

Min = 1
for i in range(1500):
    Tmp = Min / 2
    if Tmp == 0:
        print("Underflow limit found: ", Min, "Iteration number: ", i)
        break
    else:
        Min = Tmp

Max = 1.0
for i in range(10000):
    Tmp = Max * 2
    if Tmp == math.inf:
        print("Overflow limit found: ", Max, "Iteration number: ", i)
        break
    else:
        Max = Tmp
