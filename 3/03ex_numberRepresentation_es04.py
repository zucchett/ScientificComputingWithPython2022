# 4. Machine precision

# Similarly to the previous exercise, write a program to determine the 
# machine precision for floating point numbers.

# *Hint*: define a new variable by adding an increasingly smaller value 
# and check when the addition starts to have no effect on the number.

from math import isinf

num = 1.0
num_adder = 10**(304)
num_prev = 0
while True:
    if (num != num + num_adder) and not isinf(num):
        num_prev = num
        num = num + num_adder
    else: 
        num_adder = num_adder * 10**(-1)
    if num_adder < 10**(-323):
        break

print("Machine precision by using 1.0: ",num_prev)