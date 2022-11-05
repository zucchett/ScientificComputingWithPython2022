#Task 1

def converter(x):
    print("Binary representation: ", bin(x))
    print("Decimal representation: ", x)
    print("Hexadecimal representation: ", hex(x))

    
#Testing function converter
converter(14)

##########################################################################

#Task 2

import struct

def floatpoint(x):
    
    if len(x) <= 32:
        sign = x[:1]
        exponent = x[1:9]
        mantissa = x[9:32]
        print('sign: ', sign)
        print('exponent: ', exponent)
        print('mantissa: ', mantissa)
        
    else:
        print('The inserted value has to be a 32 bit word.\n')
           
    f = int(x, 2)
    fp=struct.unpack('f', struct.pack('I', f))[0]
    print(fp)

x='00000000110000101011000000000000'
floatpoint(x)

########################################################################
#Task 3

N = 1500
underflow = 1
overflow = 1
factor = 2


        
for n in range (N):
    try:
        
        underflow = underflow / factor
        overflow = overflow * factor
        print(n, 'underflow:\t %2e'%underflow, '   overflow:\t %2e'%overflow)
        
    except Exception as e:
    
        print(e)
        print("Overflow")
        break
#############################################################################
#Task 4

x=1
def presicion(a):
    b=1
    i=0
    while a != a+b :
        a = a + b
        b = b/2
        i += 1
    print ('max precision', pow(2,-i+1))
    
presicion(x)
########################################################################

#Task 5a

import math


def quadratic(a, b, c):

    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)

    return x1, x2

print(quadratic(0.001, 1000, 0.001))

#Task 5b
def quadratic_b(a, b, c):
    
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) * (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a) * (-b - math.sqrt(b * b - 4 * a * c))
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) * (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a) * (-b + math.sqrt(b * b - 4 * a * c))
    
    return x1, x2
    
print(quadratic_b(0.001, 1000, 0.001))

#Comment for difference between 5a and 5b
#The result otained is not exactly the same: after multiplying numerator and denominator for the same expression we obtain different decimals due to computer arithmetic.
#when using floating point numbers algorithms with the equivalent algebra expressions can give different results.



#Task 5c
def quadratic_root(a, b, c):
    
    x1 = math.fsum([-b, math.sqrt(b * b - 4 * a * c)]) / (2 * a)
    x2 = math.fsum([-b, -math.sqrt(b * b - 4 * a * c)]) / (2 * a)
    
    return x1, x2

print(quadratic_root(0.001, 1000, 0.001))

#########################################################################
#Task 6a

f = lambda x : x*(x-1)

d = (f(1 + 10**-2) - f (1)) / 10**-2
print('df/dx = ', d)

#Task 6b
for b in  [4,6,8,10,12,14]:
    print('Value of the derivative for delta = 10^-{} = '.format(b), (f(1 + 10**-b) - f(1)) / 10**-b)

#Comment for the Task 6b
#With decreasing delta, accuracy is also decreasing

#########################################################################
#Task 7a

import math 


f=lambda x: math.sqrt(1-x**2)

def integral_rad(n):
    h=2/n
    i = 1
    ins = 0.5 * h * (f(-1) + f(1))
    while i < n:
        ins += h*f(-1+i*h)
        i += 1
    return ins

print(integral_rad(100))
#Result is slightly differenet than the one mentioned in the text of the task

#Result is 1.5691342555492505 which is really close to the true 1.57079632679...
#The difference is minor 

#Task 7b
import timeit

n = 100

while(True):
    start=timeit.default_timer()
    integral_rad(n)
    end=timeit.default_timer()
    time= abs(end-start)
    if(time>=1):
        break
    elif(time >0 and time <0.90):
        n*=2
    else:
        n+=1

print("the max N to compute the integral in < 1 sec is ", n)
print("the difference between the true value and the calculated value ( 1 min ) is ", math.pi/2 - integral_rad(n*60))

#Comment
#The more we increase the value of N , calculated value gets closer to the true value
# But with increasing value of N, we also increase execution time
#Difference I got is 8.051337374581635e-13


