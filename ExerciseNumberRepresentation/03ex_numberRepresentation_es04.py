"""
4. **Machine precision**

Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.

*Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have 
no effect on the number.
"""

a = 1
for i in range(10000):
    tmp = a / 10
    if tmp != a:
        a = tmp
    else:
        print("Number of decimal of precision = ", i)
        break
