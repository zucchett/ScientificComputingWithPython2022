"""
____________________________ ESERCIZIO 1 ____________________________

1. Number representation

Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex). 
Determine the input type in the function, and pass another argument to choose the output representation.
Consider only int, not floating 


"""

def convert( num, tipo ):
	if ( tipo == 'dec' ):	#conversion in dec
		num_dec = int(num)
		return num_dec
	if ( tipo == 'bin' ):	#conversion in bin
		num_bin = bin(num)
		return num_bin
	if ( tipo == 'hex' ):	#conversion in hex
		num_hex = hex(num)
		return num_hex
	else : 
		return 'error'

#the function automatically recognise the type of the input, convert it to the required type and return it converted

# tests
#print(convert( 0b001101 , 'hex'))
#print(convert( 1101 , 'hex'))
#print(convert( 147 , 'bin'))
#print(convert( 0x1A097F , 'dec'))



"""
____________________________ ESERCIZIO 2 ____________________________

2. 32-bit floating point number

Write a function that converts a 32 bit binary string (for example, 110000101011000000000000) into a single precision floating point in decimal representation. 
Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.


"""

def convertBin2Dec(n):

	if (len(n) > 32) :	#check the length
		return 'error'
	while len(n) != 32 : #0 padding technique for the shorter input
		n = n + '0'
	#from the formula
	segno = (-1)**int(n[0]) #compute the sign
	exp = int(n[1:9],2)	#compute the exp
	f1 = 1.0
	for i in range(9, 32) : #compute the mantissa
		f1 = f1 + int(n[i])/2**(i-8)
	ndec = segno*f1*(2**(exp-127))
	return ndec 
	
print(convertBin2Dec('110000101011000000000000'))



"""
____________________________ ESERCIZIO 3 ____________________________

3. Underflow and overflow

Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your computer.
Hint: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.


"""
#UNDERFLOW
x = 1.0
i = 0

while x != 0 :
	xprev = x
	x = x*2**(-i)
	i = i+1
print(xprev) 	#underflow error

#OVERFLOW
y = 1.0
i = 0

while y < float('inf') :
	yprev = y
	y = y*2**(i)
	i = i+1
print(yprev) 	#overflow error


"""
____________________________ ESERCIZIO 5 ____________________________

Machine precision

Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
Hint: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.

"""

x = float(1.0)
xprev = float(0)
i = 0
while x != xprev : #while number that you added has no effect
	xprev = x
	x = x + 2**(-i)
	i = i + 1
print(2**(-i))



"""
____________________________ ESERCIZIO 5 ____________________________ 

5. Quadratic solution

Write a function that takes in input three parameters ,  and  and prints out the two solutions to the quadratic equation 
 using the standard formula:
 
(a) use the function to compute the solution for a = 0.001, b = 1000 and c = 0.001

(b) re-express the standard solution formula by multiplying the numerator and the denominator by 
 and again find the solution for a = 0.001, b = 1000 and c = 0.001. How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)

(c) write a function that computes the roots of a quadratic equation accurately in all cases


"""
import math

# (a)

def quadraticSol(  a, b, c ) :
	delta = b**2 - 4*a*c
	if delta > 0 :	#if delta > 0 there are two different real solutions
		sol1 = (- b + math.sqrt(delta))/(2*a)
		sol2 = (- b - math.sqrt(delta))/(2*a)
		return [sol1, sol2]
	if delta == 0 : #if delta = 0 there are two equal solutions
		sol1 = (- b + math.sqrt(delta))/(2*a)
		return [sol1, sol1]
	else : #if delta < 0 there are two complex solutions
		pos_delta = - delta #positive delta
		sq_delta = math.sqrt(pos_delta) 
		im_delta = complex(0, sq_delta)	#define a complex number, real part = 0, imaginary part = sq_delta
		sol1 = (- b + im_delta)/(2*a)
		sol2 = (- b - im_delta)/(2*a)
		return [sol1, sol2]


print(quadraticSol(0.001, 1000, 0.001))


# (b)

def quadraticSolMod(  a, b, c ) :
	delta = b**2 - 4*a*c
	if delta >= 0 :
		sol1 = (- b + math.sqrt(delta))*(- b - math.sqrt(delta))/(2*a*(- b - math.sqrt(delta)))
		sol2 = (- b - math.sqrt(delta))*(- b + math.sqrt(delta))/(2*a*(- b + math.sqrt(delta)))
		return [sol1, sol2]
	else :
		pos_delta = - delta
		sq_delta = math.sqrt(pos_delta)
		im_delta = complex(0, sq_delta)
		sol1 = (- b + im_delta)*(- b - im_delta)/(2*a*(- b - im_delta))
		sol2 = (- b - im_delta)*(- b + im_delta)/(2*a*(- b + im_delta))
		return [sol1, sol2]

print(quadraticSolMod(0.001, 1000, 0.001))


# (c)
import numpy #need to be installed

ap = numpy.longdouble(0.001)
bp = numpy.longdouble(1000)
cp = numpy.longdouble(0.001)

print(quadraticSol(ap, bp, cp))


"""
____________________________ ESERCIZIO 6 ____________________________ 

6. The derivative

Write a program that implements the function f(x) = x(x-1)

(a) Calculate the derivative of the function at the point x=1 using the derivative definition with delta = 10^(-2)
  Calculate the true value of the same derivative analytically and compare it with the answer your program gives. The two will not agree perfectly. Why?

(b) Repeat the calculation. How does the accuracy scale with delta?


"""

#(a)

def f(x) :	#define the given function
	return x*(x-1)
def derivative(x, delta) :	#define function to calculate the derivative by the definition
	d = (f(x+delta) - f(x))/delta
	return d

print(derivative(1, 10**(-2)))

# the derivative of f(x) = x^2 - x is f'(x) = 2x-1
# x = 1  => f'(1) = 2-1 = 1
#because of the limit and delta


#(b)
print(derivative(1, 10**(-4)), "error: ", 1.0 - derivative(1, 10**(-4)))
print(derivative(1, 10**(-6)), "error: ", 1.0 - derivative(1, 10**(-6)))
print(derivative(1, 10**(-8)), "error: ", 1.0 - derivative(1, 10**(-8)))
print(derivative(1, 10**(-10)), "error: ", 1.0 - derivative(1, 10**(-10)))
print(derivative(1, 10**(-12)), "error: ", 1.0 - derivative(1, 10**(-12)))
print(derivative(1, 10**(-14)), "error: ", 1.0 - derivative(1, 10**(-14)))

# the accuracy increases until the derivative with delta = 10^(-8), then it decreases because delta is too small and it can't be represented correctly


"""
____________________________ ESERCIZIO 7 ____________________________

Consider the integral of the semicircle of radius 1, which is known to be I = pi/2. 
Alternatively we can use the Riemann definition of the integral, with h = N/2 the width of each of the N slices the domain is divided into 
and where y_k is the value of the function at the k-th slice.

(a) Write a program to compute the integral with N=100. How does the result compare to the true value?

(b) How much can N be increased if the computation needs to be run in less than a second? What is the gain in running it for 1 minute? Use timeit to measure the time.


"""
import timeit

#(a)

N = 100
h = 2/N
I = 0
for i in range(1, N+1) : #for each slice
	x = -1 + 2*i/N #x position
	I = I + (h*math.sqrt(1-x**2)) #integral 
print(I)

#The result differs to the real value in order 10^(-3)


#(b)

starting_time = timeit.default_timer()

N = 10**6
h = 2/N
I = 0
for i in range(1, N+1) :
	x = -1 + 2*i/N
	I = I + (h*math.sqrt(1-x**2))
finish_time = timeit.default_timer()
print(I)
print(finish_time - starting_time)

# to run in less than a second N can be increased until N = 10**6


starting_time = timeit.default_timer()

N = 10**8
h = 2/N
I = 0
for i in range(1, N+1) :
	x = -1 + 2*i/N
	I = I + (h*math.sqrt(1-x**2))
finish_time = timeit.default_timer()
print(I)
print(finish_time - starting_time)

# the gain in running it for 1 minute is to reach the true result


