# Author: Luca Bonaventura matr. 2090005

#_________________________________________________ESERCIZIO 1__________________________________________________

"""
1. Number representation

Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex). Determine the input type in the function, and pass another argument to choose the output representation.
"""
print("___________ESERCIZIO 1___________")

# The function converts numbers among the bin, dec, and hex representations (bin<->dec<->hex)
def convrter(num, tipo):
	# Converts each base to decimal
	if(tipo == "dec"):
		return int(num)
	
	# Converts each base to binary
	if(tipo == "bin"):
		return bin(num)
	
	# Converts each base to hexadecimal
	if(tipo == "hex"):
		return hex(num)
	
	# return error strng in every other cases
	else:
		return "error"

# Test the function
print(convrter(0b101, "hex"))

#_________________________________________________ESERCIZIO 2__________________________________________________

"""
2. 32-bit floating point number

Write a function that converts a 32 bit binary string (for example, 110000101011000000000000) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.
"""
print("___________ESERCIZIO 2___________")


from codecs import decode
import struct


def bin_to_float(binary):
	# xfloat = (-1)^s * 1.f * 2^(e-bias)
	xf = (-1.0)**int(binary[0])
	# compute 1.f = 1 + m(n- 1)/2 + m(n- 2)/4 + ...
	f1 = 1.0
	for i in range(9, len(binary)-1):
		f1 = f1 + int(binary[i])/(2**(i-8))
	exp = int(binary[1 : 9 : 1 ],2)
	return xf*f1*2**(exp-127)

# Test the function
print(bin_to_float("110000101011000000000000"))

#_________________________________________________ESERCIZIO 3__________________________________________________

"""
3. Underflow and overflow

Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your computer.

Hint: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.
"""
print("___________ESERCIZIO 3___________")

#UNDERFLOW ERROR
x = float(1.0)
xprev = float(x)
i = 0
while x != 0:
	xprev = x
	x = x * 2**(-i) #halve
	i = i + 1
#underflow error
print (xprev)

#OVERFLOW ERROR
x = float(1.0)
xprev = float(0)
i = 1
while x < float('inf'):
	xprev = x
	x = x * 2**(i) #double
	i = i + 1
#overflow error
print (xprev)

#_________________________________________________ESERCIZIO 4__________________________________________________

"""
4. Machine precision

Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.

Hint: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.
"""
print("___________ESERCIZIO 4___________")

x = float(1.0)
xprev = float(0)
i = 0
while x != xprev:
	xprev = x
	x = x + 2**(-i)
	i = i + 1
#number that added has no effect
print (2**(-i))

#_________________________________________________ESERCIZIO 5__________________________________________________

"""
5. Quadratic solution

Write a function that takes in input three parameters ,  and  and prints out the two solutions to the quadratic equation 
 using the standard formula:
 
"""
print("___________ESERCIZIO 5___________")
"""
(a) use the function to compute the solution for ,  and 
"""
a = 0.001
b = 1000
c = 0.001

from math import sqrt
# Compute x1 and x2 with standard fnction
x1 = (-b - sqrt(b**2 - 4* a*c))/(2*a)
x2 = (-b + sqrt(b**2 - 4* a*c))/(2*a)
print(x1)
print(x2)


"""
(b) re-express the standard solution formula by multiplying the numerator and the denominator by 
 and again find the solution for ,  and . How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)
"""
#Multiply and divide
x1 = (-b - sqrt(b**2 - 4* a*c))*(-b + sqrt(b**2 - 4* a*c))/(2*a*(-b + sqrt(b**2 - 4* a*c)))
x2 = (-b + sqrt(b**2 - 4* a*c))*(-b - sqrt(b**2 - 4* a*c))/(2*a*(-b - sqrt(b**2 - 4* a*c)))
print(x1)
print(x2)
"""
(c) write a function that computes the roots of a quadratic equation accurately in all cases
"""



#_________________________________________________ESERCIZIO 6__________________________________________________

"""
6. The derivative

Write a program that implements the function 

(a) Calculate the derivative of the function at the point  using the derivative definition:

 
 
 
with 
. Calculate the true value of the same derivative analytically and compare it with the answer your program gives. The two will not agree perfectly. Why?

(b) Repeat the calculation for 
 and 
. How does the accuracy scale with ?
"""
print("___________ESERCIZIO 6___________")

# define f given function
def f(x):
    return (x*(x-1))

# define function to compute derviate
def der(x, d):
	return (f(x+d) - f(x))/d

# (a)
x = 1
d = 10**(-2)
print(der(x, d))

# (b)
for i in range(6):
	d = d*10**(-2)
	print(der(x, d))

"""
The derivate is: f'(x) = x-1+x = 2x -1 -> f'(1) = 1
We can observe that the difference from the printed value to the real value decreases until 10^-10, but then it increases and became unstable
"""
#_________________________________________________ESERCIZIO 7__________________________________________________

"""
Consider the integral of the semicircle of radius 1:
which is known to be 
 
.

Alternatively we can use the Riemann definition of the integral:
 
 

with  the width of each of the  slices the domain is divided into and where 
 is the value of the function at the th slice.

(a) Write a program to compute the integral with . How does the result compare to the true value?

(b) How much can  be increased if the computation needs to be run in less than a second? What is the gain in running it for 1 minute? Use timeit to measure the time.
"""
print("___________ESERCIZIO 7___________")

# (a)
N = 100
I = 0
for i in range(1, N+1, 1):
	x = -1 + 2*i/(N) 
	I = I + 2/N * sqrt (1 - x**2)
print(I)
# the difference is 9.8e-3

# (b)
import timeit
starting_time = timeit.default_timer()
N = 10**6
I = 0
for i in range(1, N+1, 1):
	x = -1 + 2*i/(N) 
	I = I + 2/N * sqrt (1 - x**2)
print(I)
I1 = I
#trying N=1e4 is the limit to run for 1 sec
print("Time difference :", timeit.default_timer() - starting_time)

starting_time = timeit.default_timer()
N = 10**8
I = 0
for i in range(1, N+1, 1):
	x = -1 + 2*i/(N) 
	I = I + 2/N * sqrt (1 - x**2)
print(I)
#trying N=1e8 is the limit to run for 1 min
print("Time difference :", timeit.default_timer() - starting_time)
I2 = I

# The gain in 1 min from 1 sec is:2e-6

