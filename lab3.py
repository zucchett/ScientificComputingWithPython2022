from codecs import decode
import struct
import sys
import math
import timeit


print("******************* Question 1 *********************")

print("Enter your number and which one do you want to convert:")

num = input("Number: ")
mod = input("You can choose H for Hexa, D for Decimal and B for Binary: ")



def checkNum(num):
    if num.startswith("0x"):
        return "h"    
    elif num.startswith("0b"):
        return "B"
    else:
        return "D"

def converter(num, mod):
    
    numberType = checkNum(num)
    
    if mod == "H" or mod == "h":
        if numberType == "H":
            return num
        elif numberType == "B":
            num = int(num, 2)
            return hex(num)
        elif numberType == "D": 
            return hex(int(num))
        
    elif mod == "B" or mod == "b":
        if numberType == "H":
            num = int(num, 16)
            return bin(num)
        elif numberType == "B":            
            return num
        elif numberType == "D":
            return bin(int(num))

    elif mod == "D" or "d":
        if numberType == "H":
            return int(num, 16)
        elif numberType == "B":
            return int(num, 2)
        elif numberType == "D":
            return num
    else:
        return "You have entered a wrong operation!"
    
print(converter(num, mod))
 

print("******************* Question 2 *********************")

bit_string = "110000101011000000000000"

sign_bit = int(bit_string[0])
print("sign bit: ", sign_bit)

exponent_bits = int(bit_string[1:9])
print("exponent bits: ", exponent_bits)

mantissa_bits = int(bit_string[9:32])
print("mantissa bits: ", mantissa_bits)

def binToFloat(b):
    bf = int_to_bytes(int(b, 2), 8)
    return struct.unpack('>d', bf)[0]

def int_to_bytes(n, length):
    return n.to_bytes(length, byteorder='big')

print(binToFloat(bit_string))


print("******************* Question 3 *********************")

x = 1
y = 1

while y >= 1/pow(2, 31):
    y = y/2

while x <= sys.maxsize:
    x = x*2
    
print(x)

print(y)
    

print("******************* Question 4 *********************")

minimum = 1
adding_value = 2**(-1)
while True:
    new_minimum = minimum + adding_value
    adding_value = adding_value**2
    print(new_minimum)
    if minimum == new_minimum:
        print("We are in the end...We don't see any effect anymore!")
        print("Number: ", minimum)
        break
    minimum = minimum + new_minimum



print("******************* Question 5 Section A *********************")

def calculateQuadratic(a, b, c):
    sol = (-b + math.sqrt(pow(b, 2) - 4*a*c))/(2*a)
    sol2 = (-b - math.sqrt(pow(b, 2) - 4*a*c))/(2*a)
    return (sol, sol2)

a = 0.001
b = 1000
c = 0.01

print(calculateQuadratic(a, b, c))

print("******************* Question 5 Section B *********************")

def calculateQuadratic(a, b, c):
    sol = (-b + math.sqrt(pow(b, 2) - 4*a*c))*math.sqrt(pow(b, 2) - 4*a*c)/(2*a)*math.sqrt(pow(b, 2) - 4*a*c)
    sol2 = (-b - math.sqrt(pow(b, 2) - 4*a*c))*math.sqrt(pow(b, 2) - 4*a*c)/(2*a)*math.sqrt(pow(b, 2) - 4*a*c)
    return (sol, sol2)

a = 0.001
b = 1000
c = 0.01

print(calculateQuadratic(a, b, c))

print("******************* Question 5 Section C *********************")

def calculateDelta(a, b, c):
    return pow(b, 2) - 4*a*c

def calculateQuadratic(a, b, c):
    
    delta = calculateDelta(a, b, c)
    
    if delta == 0:
        sol = -b/(2*a)
        return (sol, sol)
        
    elif delta > 0:
        sol = (-b + math.sqrt(delta))/(2*a)
        sol2 = (-b - math.sqrt(delta))/(2*a)
        return (sol, sol2)
    
    else:
        reel = (-b)/(2*a)
        im = (math.sqrt(abs(delta)))/(2*a)
        reel_root = reel,"+", im, "i"
        im_root = reel,"-", im, "i"
        print(tuple(reel_root), tuple(im_root))

a = 1
b = -1
c = 1

print(calculateQuadratic(a, b, c))

print("******************* Question 6 *********************")

def func(x):
    return (x*(x-1))

def derivative(x, teta):
    res = (func(x+teta) - func(x))/teta
    return res

teta = 10**(-2)

teta1 = 10**(-4)

teta2 = 10**(-6)

teta3 = 10**(-8)

teta4 = 10**(-10)

teta5 = 10**(-12)

teta6 = 10**(-14)
print("******************* Question 6 Section A *********************")
print("For teta: ", teta, ", Result is: ", derivative(1, teta))
print("******************* Question 6 Section B *********************")
print("For teta1: ", teta1, ", Result is: ", derivative(1, teta1))
print("For teta2: ", teta2, ", Result is: ", derivative(1, teta2))
print("For teta3: ", teta3, ", Result is: ", derivative(1, teta3))
print("For teta4: ", teta4, ", Result is: ", derivative(1, teta4))
print("For teta5: ", teta5, ", Result is: ", derivative(1, teta5))
print("For teta6: ", teta6, ", Result is: ", derivative(1, teta6))
    

print("******************* Question 7 *********************")

def calculateRiemann(N):
    my_sum = 0
    y = 2/N
    for i in range(N+1):
        x = (y*i) - 1
        my_sum = my_sum + math.sqrt(1-x**2)*y
    return my_sum

print("******************* Question 7 Section A *********************")
print(calculateRiemann(100))
print("******************* Question 7 Section B *********************")

starttime = timeit.default_timer()
print(calculateRiemann(120000000))
endtime = timeit.default_timer()

print("For ", endtime - starttime, " Result is like upwards which we can say that it becomes more like PI/2")