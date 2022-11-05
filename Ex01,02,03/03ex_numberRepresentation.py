"""1. Number representation

Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex). Determine the input type in the function, and pass another argument to choose the output representation."""

import math
print("please write Hexadecima, Decimal or Binary")
input_var = input()
def func(input_var):
    def output_type():
        print("please write output type(write 'dec' or 'bin' or 'hex'): ")
        output_type = input()
        if output_type == "dec":
            print("decimal output = ",input_res)
        elif output_type == "bin":
            print("binary output = ", bin(input_res))
        elif output_type == "hex":
            print("hexadecimal output = ", hex(input_res))
        else:
            print("You have to write 'hex', 'dec', or 'bin'")
    list_input = list(input_var)
    if list_input[1] == "x":
        input_res = int(input_var,16)
        print("Variable is Hexadecimal")
        output_type()
    elif list_input[1] == "b":
        input_res = int(input_var,2)
        print("Variable is Binary =")
        output_type()
    else:
        input_res = int(input_var)
        print("Variable is Decimal =")
        output_type()
func(input_var)

"""2. 32-bit floating point number

Write a function that converts a 32 bit binary string (for example, 110000101011000000000000) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations."""

import math
def single_precision(floating_number):
    floating_number,result,counter,result_exponent = list(floating_number),0,0,0
    for i in floating_number[8:31]:
        result = result + (int(i)/(pow(2,counter)))
        counter = counter + 1
    counter = 7
    for i in floating_number[1:9]:
        result_exponent = result_exponent + (int(i)*pow(2,counter))
        counter = counter - 1
    result =result * pow(2,result_exponent-127) 
    if floating_number[0] == 0:
        print(result)
    else:
        print(-result)
x = "11000000101100000000000000000000"
single_precision(x)

"""3. Underflow and overflow

Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your computer.

Hint: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits."""


loop1,loop2=1023,1074
over_flow,under_flow= 1,1
for i in range(loop1):
    over_flow = over_flow*2
print("%.5e"%over_flow) # 1023 is the limit. If we loop 1024 than variable exceeds limit and we cant compile the code.
for i in range(loop2):
    under_flow = under_flow/2
print("%.5e"%under_flow) # Under Flow = 1074 is the limit. Last number is 5e-324. If we loop 1075 or higher, than it starts to print 0.0.

"""4. Machine precision

Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.

Hint: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number."""
variable,counter,number = 1,0,10
while (variable > 0):
    if  variable == variable + (number/pow(2,counter)):
        print("it took ", counter, "times for this loop to uneffect the number")
        break
    else:
        variable = variable + (number/pow(2,counter))
        counter  = counter + 1

"""5. Quadratic solution

Write a function that takes in input three parameters  𝑎 ,  𝑏  and  𝑐  and prints out the two solutions to the quadratic equation  𝑎𝑥2+𝑏𝑥+𝑐=0  using the standard formula:
𝑥=−𝑏±𝑏2−4𝑎𝑐⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯√2𝑎
 
(a) use the function to compute the solution for  𝑎=0.001 ,  𝑏=1000  and  𝑐=0.001 """
import math
def f(a,b,c):
    x1 = ((-b) + math.sqrt(pow(b,2)-(4*a*c)))/(2*a)
    x2 = ((-b) - math.sqrt(pow(b,2)-(4*a*c)))/(2*a)
    list_roots = [x1,x2]
    return list_roots
# a,b,c = float(input()),float(input()),float(input())
print("roots of")
print(f(0.001,1000,0.001))
"""(b) re-express the standard solution formula by multiplying the numerator and the denominator by  −𝑏∓𝑏2−4𝑎𝑐⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯√  and again find the solution for  𝑎=0.001 ,  𝑏=1000  and  𝑐=0.001 . How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)"""
import math
def f(a,b,c):
    x1 = (((-b) + math.sqrt(pow(b,2)-(4*a*c)))*((-b) + math.sqrt(pow(b,2)-(4*a*c))))/(2*a*((-b) + math.sqrt(pow(b,2)-(4*a*c))))
    x2 = (((-b) - math.sqrt(pow(b,2)-(4*a*c)))*((-b) + math.sqrt(pow(b,2)-(4*a*c))))/(2*a*((-b) + math.sqrt(pow(b,2)-(4*a*c))))
    x3 = (((-b) + math.sqrt(pow(b,2)-(4*a*c)))*((-b) - math.sqrt(pow(b,2)-(4*a*c))))/(2*a*((-b) - math.sqrt(pow(b,2)-(4*a*c))))
    x4 = (((-b) - math.sqrt(pow(b,2)-(4*a*c)))*((-b) - math.sqrt(pow(b,2)-(4*a*c))))/(2*a*((-b) - math.sqrt(pow(b,2)-(4*a*c))))
    list_roots = [x1,x2,x3,x4]
    return list_roots
#we are multiplying and dividing roots with the same value, so it does not effect the nubmer 
print(f(0.001,1000,0.001))
"""(c) write a function that computes the roots of a quadratic equation accurately in all cases"""
import math
def f(a,b,c):
    discriminant = pow(b,2)-(4*a*c)
    if discriminant >0:
        x1 = ((-b) + math.sqrt(pow(b,2)-(4*a*c)))/(2*a)
        x2 = ((-b) - math.sqrt(pow(b,2)-(4*a*c)))/(2*a)
        list_roots = [x1,x2]
        print("function has two roots")
        # x1 = str((-b)/(2*a) + (math.sqrt(-(pow(b,2)-(4*a*c))))*"j")
        return list_roots
    elif discriminant == 0:
        return ("Function has double root", ((-b) + math.sqrt(pow(b,2)-(4*a*c)))/(2*a))
    else: 
        print("function has two complex roots")
        print("\t\t","x1=",(-b)/(2*a),"+", (math.sqrt(-(pow(b,2)-(4*a*c))))/(2*a),"j\t\t")
        print("\t\t","x2=",(-b)/(2*a),"-", (math.sqrt(-(pow(b,2)-(4*a*c))))/(2*a),"j\t\t")
# a,b,c = float(input()),float(input()),float(input())
print("roots of")
print(f(1,4,5))

"""6. The derivative

Write a program that implements the function  𝑓(𝑥)=𝑥(𝑥−1) 
(a) Calculate the derivative of the function at the point  𝑥=1  using the derivative definition:

d𝑓d𝑥=lim𝛿→0𝑓(𝑥+𝛿)−𝑓(𝑥)𝛿
 
with  𝛿=10−2 . Calculate the true value of the same derivative analytically and compare it with the answer your program gives. The two will not agree perfectly. Why?"""

def f(x):
    return (x*(x-1))
x,sigma = 1,-2
result = (f(x+pow(10,sigma))-f(x))/(pow(10,sigma))
print (result)
"""Manual calculation and computer calculation not agreeing perfectly. We subtract it as an integer since we assume that it approaches 0 during manual calculation. 
But this assumption is not made on the computer. """

"""(b) Repeat the calculation for  𝛿=10−4,10−6,10−8,10−10,10−12  and  10−14 . How does the accuracy scale with  𝛿 ?"""

def f(x):
    return (x*(x-1))
x,sigma = 1,[-4,-6,-8,-10,-12,-14]
for i in sigma:
    result = (f(x+pow(10,i))-f(x))/(pow(10,i))
    print ("for   10^",i,"  result =", result)
    """Accuracy getting lower when sigma gets lower. Accuracy gets lower disctinctly after sigma =10^-8 point."""


"""7. Integral of a semicircle

Consider the integral of the semicircle of radius 1:
𝐼=∫1−1(⎯⎯√1−𝑥2)d𝑥
 
which is known to be  𝐼=𝜋2=1.57079632679... .

Alternatively we can use the Riemann definition of the integral:
𝐼=lim𝑁→∞∑𝑘=1𝑁ℎ𝑦𝑘
 
with  ℎ=2/𝑁  the width of each of the  𝑁  slices the domain is divided into and where  𝑦𝑘  is the value of the function at the  𝑘− th slice.

(a) Write a program to compute the integral with  𝑁=100 . How does the result compare to the true value?"""

import math
n = 500000
def f(n):
    result = 0
    for x in range(0,n):
        result = result + math.sqrt(1-pow((x/n),2))
    return (result*2/n)
print(f(n))
 

"""The result is changing after third number.
when we increase N(that means increasing number of loop) than it becomes more accurate
I tried to make the loop 500.000, it computed under a second and it was accurate until the 6th number "1.5707983251317754" """

"""(b) How much can  𝑁  be increased if the computation needs to be run in less than a second? What is the gain in running it for 1 minute? Use timeit to measure the time."""
import timeit
import math
n = 990000
def f(n):
    result = 0
    for x in range(0,n):
        result = result + math.sqrt(1-pow((x/n),2))
    return (result*2/n)
print(f(n))
print(timeit.timeit("f(960000)",setup="from __main__ import f",number=1)) #between 955000(0.9835665999999037 seconds) and 960000(1.065322800001013 seconds) loops it computes under a second
print(timeit.timeit("f(55500000)",setup="from __main__ import f",number=1)) #if we give N=55500000, it takes 59.955750799999805 seconds to compute
