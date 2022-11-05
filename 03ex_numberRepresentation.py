import math
import timeit
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 10:35:56 2022

@author: daria
"""

#Number representation
print("--- NUMBER REPRESENTATION ---\n")

def convertBinDecHex(inp, output_type):
    if output_type == bin:
        return bin(inp)
    elif output_type == hex:
        return hex(inp)
    elif output_type == int:
        return int(inp)
n_dec = 13
n_bin = bin(n_dec)
n_hex = hex(n_dec)
print("From decimal to hexadecimal and binary:")
print("Hexadeciaml representation of", n_dec, 'is: ', convertBinDecHex(13, hex))
print("Binary representation of", n_dec, 'is: ', convertBinDecHex(13, bin))
print("")
print("From binary to decimal and hexadecimal:")
print("Decimal representation of", n_bin, 'is: ', convertBinDecHex(0b1101, int))
print("Hexadeciaml representation of", n_bin, 'is: ', convertBinDecHex(0b1101, hex))
print("")
print("From hexadecimal to decimal and binary:")
print("Decimal representation of", n_hex, 'is: ', convertBinDecHex(0xd, int))
print("Binary representation of", n_hex, 'is: ', convertBinDecHex(0xd, bin))

#32-bit floating point number
print("\n--- 32-BIT FLOATING POINT NUMBER ---\n")

def convertToFloat(string_number):
    sign = int(string_number[0])
    exp = int(string_number[1:9], 2)
    exp_unbias = exp - 127
    mantissa_str = string_number[9:]
    power = -1
    mantissa = 0
    for i in mantissa_str:
        mantissa += (int(i) * pow(2, power))
        power -= 1
    mantissa = 1.0 + mantissa
    float_number = pow(-1, sign) * mantissa * pow(2, exp_unbias)
    return float_number
string1 = "00000011111000000000000000000000"
real_1 = convertToFloat(string1)
print("The float value of", string1, "is :",real_1)
string2 = "11000000101100000000000000000000"
real_2 = convertToFloat(string2)
print("The float value of", string2, "is :",real_2)
string3 = "110000101011000000000000"
real_3 = convertToFloat(string3)
print("The float value of", string3, "is :",real_3)

#Underflow and overflow
print("\n--- UNDERFLOW AND OVERFLOW ---\n")

x = 1.0
y = x * 2.0
while ((x).hex() == (y/2).hex()):
     x = x * 2.0
     y = x * 2.0     
print("The overflow limit is: ", x)

x = 1.0
y = x / 2.0
while ((x).hex() == (y*2).hex()):
     x = x / 2.0
     y = x / 2.0   
print("The underflow limit is: ", x)
  
# Machine precision
print("\n--- MACHINE PRECISION ---\n")

x = 1000.0
precision = 0.1
while ((x + precision).hex() != (x).hex()):
     precision = precision / 2
     
print("Machine precision for floating point is: ", precision)

#Quadratic solution
print("\n--- QUADRATIC SOLUTION ---\n")

def quadraticEquation(a, b, c):
    disc = b * b - 4 * a * c 
    sqrt_disc = math.sqrt(abs(disc)) 
    
    print("Roots of   ", a, "x^2 + ", b, "x +", c, " = 0   are:")
    if disc > 0: 
        print("Real and different roots ") 
        print((-b + sqrt_disc)/(2 * a)) 
        print((-b - sqrt_disc)/(2 * a)) 
    elif disc == 0: 
        print("Real and same roots") 
        print(-b / (2 * a))  
    else:
        print("Complex roots") 
        print(- b / (2 * a), " + i", sqrt_disc) 
        print(- b / (2 * a), " - i", sqrt_disc) 

def quadraticEquation2(a, b, c):
    disc = b * b - 4 * a * c 
    sqrt_disc = math.sqrt(abs(disc)) 
    
    print("Roots of   ", a, "x^2 + ", b, "x +", c, " = 0   are:")
    if disc > 0: 
        print("Real and different roots ") 
        print((2 * c)/(- b - sqrt_disc ))
        print((2 * c)/(- b + sqrt_disc )) 
    elif disc == 0: 
        print("Real and same roots") 
        print(2 * c / ( - b))  
    else:
        print("Complex roots") 
        print(- b / (2 * a), " + i", sqrt_disc) 
        print(- b / (2 * a), " - i", sqrt_disc)
        
a = 0.001
b = 1000
c = 0.001
print("Solution obtained using standard formula:")
quadraticEquation(a, b, c)
print("\nSolution obtained re-expressing the standard formula:")
quadraticEquation2(a, b, c)

# One of the roots computed via the formula (-b ± sqrt(delta)) / (2 a)
# has less precision in the case b^2 >> 4ac. In fact, when b is positive
# the computation (-b + sqrt(delta)) is nearly zero. Similarly, if b is negative
# the computation (-b - sqrt(delta)) is nearly zero. To achieve a more accurate
# result, it is convinient to compute the solution according to the sign of b.
       
def quadraticEquation3(a, b, c):
    disc = b * b - 4 * a * c 
    sqrt_disc = math.sqrt(abs(disc)) 
    
    print("Roots of   ", a, "x^2 + ", b, "x +", c, " = 0   are:")
    if disc > 0: 
        print("Real and different roots ") 
        if b >= 0:
            print((2 * c)/(- b - sqrt_disc ))
            print((-b - sqrt_disc)/(2 * a)) 
        else:
            print((-b + sqrt_disc)/(2 * a)) 
            print((2 * c)/(- b + sqrt_disc ))
    elif disc == 0: 
        print("Real and same roots") 
        print(-b / (2.0 * a))  
    else:
        print("Complex roots") 
        print(- b / (2 * a), " + i", sqrt_disc) 
        print(- b / (2 * a), " - i", sqrt_disc) 

print("\nSolution obtained with accuracy in all cases:")
quadraticEquation3(a, b, c)

#The derivative
print("\n--- THE DERIVATIVE ---\n")

def fun(x):
    return x * (x - 1)

x = 1
delta = 0.01
defDerivative = (fun(x + delta) - fun(x)) / delta
print("Derivative calculated with definition formula:", defDerivative)
analyticDerivative = 2 * x - 1
print("Derivative calculated analytically:", analyticDerivative)
print('''\nComputing the derivative analytically we lose precision and we introduce 
a systematic error equals to delta''')

deltaVector = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]
defDerivativeList = []
for deltaValue in deltaVector:
    defDerivativeList.append((fun(x + deltaValue) - fun(x)) / deltaValue)
print("\nThe corresponding derivatives to values of delta", deltaVector, "are", 
      defDerivativeList)
print('''\nThe accuracy is linear with delta for delta values greater than 1e-6 
then it is limited by the floating point precision and it starts getting
worse from delta values less equal to 1e-10''')

#Integral of a semicircle
print("\n--- INTEGRAL OF A SEMICIRCLE ---\n")

def myfun(x):
    return math.sqrt(1.0 - x**2)

def Integral(N, f):
    sum = 0
    step = 2.0 / N
    x = -1
    for i in range(N):
        sum = sum + f(x)
        x = x + step
    
    return (sum * step)

print("Integral with N = 100: ", Integral(100, myfun))

testIntegral100 = '''
def myfun(x):
    return math.sqrt(1.0 - x**2)
def Integral(N, f):
    sum = 0
    step = 2.0 / N
    x = -1
    for i in range(N):
        sum = sum + f(x)
        x = x + step
    
    return (sum * step)
Integral(100, myfun)
'''
print("Time(in seconds) to run 100 times Integral function for N=100: ", 
      timeit.timeit(stmt=testIntegral100, setup="import math", number=100))

# The profiling of the computation time using %timeit Integral(100, myfun)
# gives 30.1 µs ± 197 ns. Hence to stay within 1 second, the value of N
# can be increased approximately by a factor 33000.
testIntegral_1sec = '''
def myfun(x):
    return math.sqrt(1.0 - x**2)
def Integral(N, f):
    sum = 0
    step = 2.0 / N
    x = -1
    for i in range(N):
        sum = sum + f(x)
        x = x + step
    
    return (sum * step)
Integral(100*33333, myfun)
'''
startTime = timeit.default_timer()
Integral(100 * 33333, myfun)
print("With N = 100*33333 computation time(in seconds) is: ", 
      timeit.default_timer() - startTime)
print("Time(in seconds) to run 10 times Integral function for N=100*33333: ", 
      timeit.timeit(stmt=testIntegral_1sec, setup="import math", number=10))

# Using N = 100 * 33000 * 60, the computation time is approximately 1 minute.
print("Integral when computation is run in 1 min", 
      Integral(100 * 33300 * 60, myfun))

# The result obatained with N = 100 differs from the true value within an error 
# approximately equals to 2e-3. On the contrary, using N = 100 * 33000 * 60 
# the error is approximately 1e-9