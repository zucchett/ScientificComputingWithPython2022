"""
02ex_fundamentals
Name and surname: Mattia Sabatini
Number of matricola: 2092001
Istitutional email adress: mattia.sabatini@studenti.unipd.it
Your curriculum: single courses
"""



###########################################################################################################################################



'''
1. Number representation

Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex). Determine the input type in the function, and pass another argument to choose the output representation.
'''



# Ex. 1.

print("\n\n\nEx. 1.\n")

def converter(num, typ: str):
    
    if type(num) == str:
    
        if num[0:2] == '0b':
            if typ == 'bin':
                return num
            elif typ == 'hex':
                return hex(int(num,2))
            elif typ == 'dec':
                return int(num,2)
            else:
                return 'Error: you can choose only bin, hex or dec numbers'

        elif num[0:2] == '0x':
            if typ == 'bin':
                return bin(int(num,16))
            elif typ == 'hex':
                return num
            elif typ == 'dec':
                return int(num,16)
            else:
                return 'Error: you can choose only bin, hex or dec numbers'
    
    elif type(num) == int:
        if typ == 'bin':
            return bin(num)
        elif typ == 'hex':
            return hex(num)
        elif typ == 'dec':
            return num
        else:
            return 'Error: you can choose only bin, hex or dec numbers'
        
    else:
        return 'Error: you can choose only bin, hex or dec numbers'
        


print(converter(bin(10), 'dec'))
print(converter(bin(10), 'bin'))
print(converter(bin(10), 'hex'))

print('\n')
print(converter(10, 'dec'))
print(converter(10, 'bin'))
print(converter(10, 'hex'))

print('\n')
print(converter(hex(10), 'dec'))
print(converter(hex(10), 'bin'))
print(converter(hex(10), 'hex'))



###########################################################################################################################################



'''
2. 32-bit floating point number

Write a function that converts a 32 bit binary string (for example, 110000101011000000000000) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.
'''



# Ex. 2.

print("\n\n\nEx. 2.\n")

def converter(x):
    
    if len(x) > 32:
        print('Error: insert a 32 bit binary string')
        
    else:
    
        #sign
        sign = int(x[0])

        #mantissa conversion
        f = x[9:]
        mant = 1
        for i in range(len(f)):
            mant += int(f[i]) * 2**(-i-1)

        #exponent conversion
        exp = int(x[1:9],2)

        return (-1)**sign * mant * 2**(exp-127)

print("110000101011000000000000 in decimal representation is:", converter('110000101011000000000000'))



###########################################################################################################################################



'''
3. Underflow and overflow

Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your computer.

Hint: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.
'''

# Ex. 3.

print("\n\n\nEx. 3.\n")

x0 = 1.
#x0 is divided by 2 until it becomes 0, at which point the underflow limit is reached
while x0 != 0:
    temp0 = x0
    x0 /= 2
    
print("underflow limit:", temp0)
    
x1 = 1.
#x0 is multiplied by 2 until x1/x1 is different from 1, at which point the overflow limit has been reached
while x1/x1 == 1:
    temp1 = x1
    x1 *= 2

print("overflow limit:", temp1)



###########################################################################################################################################



'''
4. Machine precision

Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.

Hint: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.
'''


# Ex. 4.

print("\n\n\nEx. 4.\n")

eps = 1.

#eps is divided by 2 until its sum with 1 is equal to 1
while 1 + eps > 1:
    temp = eps
    eps /= 2

print("Machine precision for floating point numbers:", temp)



###########################################################################################################################################



'''
5. Quadratic solution

Write a function that takes in input three parameters a, b and c and prints out the two solutions to the quadratic equation ax^2 + bx + c = 0 using the standard formula

(a) use the function to compute the solution for a=0.001, b=1000 and c=0.001

(b) re-express the standard solution formula by multiplying the numerator and the denominator by -b \mp \sqrt(b^2 - 4ac) and again find the solution for a=0.001, b=1000 and c=0.001. How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)

(c) write a function that computes the roots of a quadratic equation accurately in all cases
'''



# Ex. 5.

print("\n\n\nEx. 5.\n")

from math import sqrt

# (a)

# Function that computes the roots of a quadratic equation using the standard formula
def sol1(a,b,c):
    delta = sqrt(b**2 - 4*a*c)
    xp = (-b + delta) / (2*a)
    xm = (-b - delta) / (2*a)
    return (xp, xm)

# (b)

# Function that computes the roots of a quadratic equation using the reduced formula
def sol2(a,b,c):
    delta = sqrt(b**2 - 4*a*c)
    xp = (2*c) / (-b - delta)
    xm = (2*c) / (-b + delta)
    return (xp, xm)

# (c)

# Function that computes the roots of a quadratic equation accurately in all cases
def sol3(a,b,c):
    delta = sqrt(b**2 - 4*a*c)
    x1 = (-b + delta) / (2*a)
    x2 = (2*c) / (-b + delta)
    return x1,x2


a = 0.001
b = 1000
c = 0.001

print("Solutions to the quadratic equation for a=0.001, b=1000 and c=0.001:")

print("\n(a)\n")
print("Standard formula:")
print(sol1(a,b,c))

print("\n(b)\n")
print("Reduced formula:")
print(sol2(a,b,c))

print("\nIn case (a) the smaller solution (in modulo) is more accurate, while in case (b) the larger one (in modulo) is")

print("\n(c)\n")
print("Solutions to the quadratic equation accurately in all cases:")
print(sol3(a,b,c))



###########################################################################################################################################



'''
6. The derivative

Write a program that implements the function f(x)=x(x-1)

(a) Calculate the derivative of the function at the point x=1

using the derivative definition with delta=10^-2. Calculate the true value of the same derivative analytically and compare it with the answer your program gives. The two will not agree perfectly. Why?

(b) Repeat the calculation for delta=10^−4,10^−6,10^−8,10^−10,10^−12 and 10^−14. How does the accuracy scale with delta?
'''



# Ex. 6.

print("\n\n\nEx. 6.\n")

import matplotlib.pyplot as plt

def func(x):
    return x*(x-1)

#function that calculates the derivative definition of the function f at point x with delta=10^-y
def derivative(x,y,f):
    d = 10**(-y)
    return (f(x+d)-f(x))/d

for y in range(2,15,2):
    print("delta=10^(-{}):".format(y),derivative(1,y,func),)

print("\nThe analytical result of the derivative of f(x)=x(x-1) in x=1 is: df/dx=1")
print("\nThe results are not all in agreement due to a roundoff-error and the result improves by increasing delta up to delta = 10^-8 and worsening after")

#Plot of the derivative as a function of delta, where the x-axis is in logarithmic scale
delta = [10**(-i) for i in range(2,15,2)]
dfunc = []
for y in range(2,15,2):
    dfunc.append(derivative(1,y,func)-1)
    
plt.plot(delta,dfunc,'.')
plt.xscale("log")
plt.yscale("log")
plt.xlabel('$\delta$')
plt.ylabel('numerical df/dx - analytyc df/dx in x=1')
plt.show()



###########################################################################################################################################



'''
7. Integral of a semicircle

Consider the integral of the semicircle of radius 1 which is known to be I=pi/2=1.57079632679...
Alternatively we can use the Riemann definition of the integral with ℎ=2/N the width of each of the N slices the domain is divided into and where yk is the value of the function at the k-th slice.

(a) Write a program to compute the integral with N=100. How does the result compare to the true value?

(b) How much can N be increased if the computation needs to be run in less than a second? What is the gain in running it for 1 minute? Use timeit to measure the time.
'''

print("\n\n\nEx. 7.\n")

from math import sqrt, pi
import timeit

def func(x):
    return sqrt(1-x*x)

#Riemann definition of the integral
def riemann(N):
    h = 2/N
    I = 0.
    for k in range(N):
        I += h * func(k/N)
    return I

true = pi/2

r = [riemann(10**(i)) for i in range(2,9)]

print("True value:",pi/2)

for i in range(2,9):
    print("\nRiemann value for n=", 10**(i) , ":",r[i-2])
    print("difference between calculated and expected value:", abs(true-r[i-2]))
    %timeit riemann(10**(i))

r180000000 = riemann(180000000)
print("\nRiemann value for n=", 180000000, ":",r180000000)
print("difference between calculated and expected value:", abs(true-r180000000))
%timeit riemann(180000000)
