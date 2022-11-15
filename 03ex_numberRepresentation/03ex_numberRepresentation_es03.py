"""
3.Underflow and overflow下溢和溢出
Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on
your computer.
*Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times
 to exceed the under/over-flow limits.
"""

num = 999
un_flow = 1
ov_flow = 1

for i in range(num):
    un_flow = un_flow / 2
    ov_flow = ov_flow * 2
    print(i, "\t", ":%1.5e" % un_flow, "\t", ":%1.5e" % ov_flow)
