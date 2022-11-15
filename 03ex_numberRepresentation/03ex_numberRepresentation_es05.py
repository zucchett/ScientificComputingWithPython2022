"""
5 Quadratic solution
Write a function that takes in input three parameters a, b and c and prints out the two solutions to the quadratic equation ax^2+bx+c=0 using the standard formula:
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
(a) use the function to compute the solution for a=0.001,b=1000 and c=0.001
(b) re-express the standard solution formula by multiplying the numerator and the denominator by -b\mp\sqrt{b^2-4ac}$ and again find the solution for a=0.001, b=1000 and c=0.001.
How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)
(c) write a function that computes the roots of a quadratic equation accurately in all cases
"""
# 导入 cmath(复杂数学运算) 模块
import math
def qu_result():
    # a = float(input('input a: '))
    # b = float(input('input b: '))
    # c = float(input('input c: '))
    a = 0.001
    b = 1000
    c = 0.001

    # a)
    d = float((b ** 2) - (4 * a * c))
    sol1 = ((-b) - math.sqrt(d)) / (2 * a)
    sol2 = ((-b) + math.sqrt(d)) / (2 * a)
    print('a) THE SOLUTION ARE {0} AND {1}'.format(sol1, sol2))

    # b)
    d = float((b ** 2) - (4 * a * c))
    factor = ((-b) - math.sqrt(d))
    sol1 = (((-b) - math.sqrt(d)) * factor) / ((2 * a) * factor)
    sol2 = (((-b) + math.sqrt(d)) * factor) / ((2 * a) * factor)

    print('b) THE SOLUTION ARE {0} AND {1}'.format(sol1, sol2))
    ##a) THE SOLUTION ARE -999999.999999 AND -9.999894245993346e-07
    ##b) THE SOLUTION ARE -999999.999999 AND -9.999894245993346e-07

# c)
def qua_normal( a = 0.001, b = 1000,c = 0.001):
    # a = float(input('input a: '))
    # b = float(input('input b: '))
    # c = float(input('input c: '))
    d = float((b ** 2) - (4 * a * c))
    if d > 0 and a != 0:
        num_roots = 2
        d = float((b ** 2) - (4 * a * c))
        sol1 = ((-b) - math.sqrt(d)) / (2 * a)
        sol2 = ((-b) + math.sqrt(d)) / (2 * a)
        print("c) THE SOLUTION ARE {} AND {}" .format(sol1, sol2))
    elif d == 0 and a != 0:
        num_roots = 1
        x = (-b) / 2 * a
        print("ONE ROOT IS: ", x)
    else:
        num_roots = 0
        print("SORRY,NO ROOTS PLEASE ENTER AGAIN < 0.")
        exit()


qu_result()

qua_normal()

