# 3. Underflow and overflow

# Write a program to determine the underflow 
# and overflow limits (within a factor of 2) for floating point numbers on your computer.
# Hint: define two variables initialized to 1, and halve/double them for a sufficient 
# amount of times to exceed the under/over-flow limits.

import sys

o=0
i=0
while(True):
  try:
    i=2**o
    o=o+0.001
  except OverflowError:
    break
print(f"Overflow value is: {2**(o-0.001)}")


u=0
ii=0
while(True):
  try:
    ii=1/(2**u)
    u=u+0.001
  except:
    break
print(f"Underflow value is: {1/(2**(u-0.001))}")