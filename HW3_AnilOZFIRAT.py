# Q1

import struct

getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]

def floatToBinary64(value):
    val = struct.unpack('Q', struct.pack('d', value))[0]
    return getBin(val)

def binaryToFloat(value):
    hx = hex(int(value, 2))   
    return struct.unpack("d", struct.pack("q", int(hx, 16)))[0]

# floats are represented by IEEE 754 floating-point format which are 
# 64 bits long (not 32 bits)

# float to binary
binstr = floatToBinary64(17.5)
print('Binary equivalent of 17.5:')
print(binstr + '\n')

# binary to float
fl = binaryToFloat(binstr)
print('Decimal equivalent of ' + binstr)
print(fl)


# Q2

my_word = "01000001011100000000000000000000" # 15
my_word2 = "01000000010010010000111111011011" # around 3.14
my_word3 = "11000001110000000000000000000000" # -24

def bintofloat(word):
    sign = 1
    if word[0] == "1":
        sign = -1
        
    exponent = ""
    for i in range(8):
        exponent = exponent + word[i+1]
    
    mantissa = ""    
    for i in range(23):
        mantissa = mantissa + word[i+9]
        
    exponent_convert = int(exponent, 2) - 127    
        
    mantissa_convert = 0
    for i in range(23):
        if mantissa[i] == "1":
            mantissa_convert = mantissa_convert + 2**(-1*(i+1))
            
    return sign * (1 + mantissa_convert) * (2 ** exponent_convert)
    
print(bintofloat(my_word)) # 15
print(bintofloat(my_word2)) # around 3.14
print(bintofloat(my_word3)) # -24

# Q3

import math as m

number = 1.0
overflow = 0
counter = 1
while number != m.inf:
    overflow = number
    number = number * 2
#    print (counter, 'Over: ', number)
    counter += 1
print("Becomes inf after ", counter-1, " iteration while doubling (prints are in comment lines for a clear view)")
print("Value after ", counter-2, "iteration: ", overflow)

number = 1.0
underflow = 0
counter = 1
while number != 0:
    underflow = number
    number = number / 2
#    print (counter, 'Over: ', number)
    counter += 1
print("Becomes 0 after ", counter-1, " iteration while halving (prints are in comment lines for a clear view)")
print("Value after ", counter-2, "iteration: ", underflow)


# Q4 

A=10

Range=10

Number=1

m=1

Factor=2

d=1

for Number in range(Range):
    
    m=m/Factor
    
    Number=Number+m
    
    d+=1
    
    print(d, " " , Number)



# Q5


import math as m

def standart(a, b, c):
    x1 = ((-b) + m.sqrt(b**2 - 4 * a * c)) / (2*a)
    x2 = ((-b) - m.sqrt(b**2 - 4 * a * c)) / (2*a)
    return x1, x2
print('A: ', standart(0.001,1000,0.001))

def standart_multiplied(a, b, c):
    x1 = (((-b) + m.sqrt(b**2 - 4 * a * c)) * ((-b) - m.sqrt(b**2 - 4 * a * c))) / ((2*a) * ((-b) - m.sqrt(b**2 - 4 * a * c)))
    x2 = (((-b) - m.sqrt(b**2 - 4 * a * c)) * ((-b) + m.sqrt(b**2 - 4 * a * c))) / ((2*a) * ((-b) + m.sqrt(b**2 - 4 * a * c)))
    return x1, x2
print('B: ', standart_multiplied(0.001,1000,0.001))

# The results had to be exactly the same while there was a small difference in the decimals. 
# This is happening because of the limited precision of the floating numbers. Even equal algorithms should give the same result
# their results may differ due to it.

def accurately(a, b, c):
    delta = b**2 - 4 * a * c 
    if delta == 0:
        return delta
    elif delta > 0:
        x1 = (((-b) + m.sqrt(delta)) / (2*a))
        x2 = (((-b) - m.sqrt(delta)) / (2*a))
        return x1, x2
    else:
        return "No Real Root"
print('C: ', accurately(0.001,1000,0.001))


# Q6

def f(x):
    return x*(x-1)

x = 1
sigma = 10**-2
#sigma = 10**-5
derivative = (f(x + sigma) - f(x)) / sigma
print("Derivative: ", derivative)
# while the analytic result had to be 1+𝛿, the result is different than the analytic result with a very small fraction.
# when we increase the sigma, the result comes closer to the correct result. this is happening because the function is
# well-conditioned but the algorithm is numerically unstable.
 
sigma = [10**(-4) ,10**(-6),10**(-8) ,10**(-10) ,10**(-12) ,10**(-14)]
for s in sigma:
    derivative = (f(x+s) - f(x)) / s
    print("Sigma: ", s, "Derivative: ", derivative, "Difference(error): ", abs((1+s)-derivative))
    
# the accuracy increasing while the sigma is increasing.



# Q7
import math
import timeit

a = -1
b = 1

def f(x):
    return math.sqrt(1-x**2)

def riemann(f, N, k):
    result = 0
    for k in range(k,N):
        h = (b-a) / N
        x_k = a + h*k
        result += h * f(x_k)
    return result



result = riemann(f, 100, 0)

    
print("Result: ", result, "N: 100", "Error: ", abs(result-math.pi/2))

# b

starttime = timeit.default_timer()
print("The start time is :",starttime)

error = riemann(f, 99999999*5, 0)
print("Result: ", result, "N: 100", "Error: ", abs(result-math.pi/2))
print(2)

print("The time difference is :", timeit.default_timer() - starttime)