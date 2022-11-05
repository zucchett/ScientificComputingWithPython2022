#EXERCISE 3

#EXCERSICE 1 

print("-----------------Exercise 1: Number representation--------------- \n")

def converter(x,toutput):
    
    print("The decimal value of", x, "is:")
    if toutput =="bin":
        print( "The type is ", type(x)," the value is ",bin(x), " in binary.")
    elif toutput == "oct":
        print( "The type is ",type(x)," the value is ",oct(x), "in octal.")
    elif toutput == "hex":
        print("The type is ", type(x)," the value is ",hex(x), "in hexadecimal.")
    else:
        print("You're not putting the right parameter")
    
converter(10,"oct")



#EXCERSICE 2 

print("-------------------------Exercise 2-----------------------")

import struct

def bin2float(b):
    h = int(b, 2).to_bytes(8, byteorder="big")
    return struct.unpack('>d', h)[0]
    
print(bin2float('0011111111111001111000110111011110011011100101111111010010100100'))



#EXCERSICE 3 

print("-------------------------Exercise 3-----------------------")

#EXCERSICE 4 

print("-------------------------Exercise 4-----------------------")

#Using the library
import sys
epsilon=sys.float_info.epsilon
print("The value of epsilon is:",epsilon)

#Manually
epsilon=1.0
while epsilon+1>1:
    epsilon=epsilon/2
epsilon=epsilon*2
print("The value of epsilon is:",epsilon)


#EXCERSICE 5

print("-------------------------Exercise 5-----------------------")

# import complex math module
import cmath



def funq(a,b,c):

    d = (b**2) - (4*a*c)

    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    print('The solution are {0} and {1}'.format(sol1,sol2))
    
funq(1,5,6)


#EXCERSICE 6 

print("-------------------------Exercise 6-----------------------")

from math import *

def f(x):
    return x ** 2
#For instance f(2) = 4
def derive(function, value):
    h = 0.00000000001
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom
    # Returns the slope to the third decimal
    return float("%.3f" % slope)
    
print (derive(f,2))



#EXCERSICE 7 

print("-------------------------Exercise 7-----------------------")

