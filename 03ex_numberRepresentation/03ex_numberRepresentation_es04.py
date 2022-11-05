"""
4 Machine precision
Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
*Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have
no effect on the number.

4 机器精度
与前面的练习类似，写一个程序来确定浮点数的机器精度。
*提示*：通过增加一个越来越小的值来定义一个新的变量，并检查何时加法开始对数字没有影响。
对数字没有影响。
"""

num = 20
var = 7
sam = 1/9

for i in range(num):
    var = var + sam
    sam = sam * (1/9)
    print(i, "\t\t", var)

print("After 14th step there is no effect on the number")