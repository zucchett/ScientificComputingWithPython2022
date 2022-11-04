# 4. Machine precision
# Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
# Hint: define a new variable by adding an increasingly smaller value and check when the addition
#  starts to have no effect on the number.

i=0.1
v=1
while(v != v+i):
    i=i/2
print(i)