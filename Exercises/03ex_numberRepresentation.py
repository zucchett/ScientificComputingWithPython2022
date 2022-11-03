#!/usr/bin/env python
# coding: utf-8

import math as m


# TASK 1

def find_input_type(number):
    """ Assuming that all binary numbers will follow the Python syntax
    and begin with "0b", and hexadecimal numbers with "0x"
    """
    if str(number)[:2]=="0b":
        return "bin"
    elif str(number)[:2]=="0x":
        return "hex"
    else:
        return "dec"
    
def convert_rep(number, output_type):
    input_type = find_input_type(number)
    type_dict = {"bin":2,"dec":10,"hex":16}
    
    if output_type == "dec":
        return int(str(number), type_dict[input_type])
    elif output_type == "bin":
        return bin(int(str(number),type_dict[input_type]))
    elif output_type == "hex":
        return hex(int(str(number), type_dict[input_type]))
    




#TASK 2
def convert_bin(bin_str):
    if len(bin_str)!=32:
        print("ERROR: Not a 32 bit binary string")
        return None
    sign = int(bin_str[0],2)
    exponent = int(bin_str[1:9],2)
    
    fraction_str = bin_str[9:]
    fraction = 0
    n = 1
    for f in fraction_str:
        fraction += int(f) * 2**(-n)
        n+=1
 
    return (-1)**sign * (1+fraction) * 2**(exponent-127)

bin_str = "11000010101100000000000000000000"
print(convert_bin(bin_str))




#TASK 3

a = 1.0
while a < m.inf:
    max_val = a
    a*=2
    
print("Result:", max_val)
    
b = 1.0
while b>0:
    min_val = b
    b/=2
    
print("Result:", min_val)




#TASK 4
a2 = 1.0
b2 = 1.0
k2 = 0
while True:
    addition = 10**(-k2)
    print(k2, b+addition)
    if a2 == b2+addition:
        print(f"Result: Addition has no effect on the number when it is 1e-{k2} or smaller")
        break
    k2 += 1

#Result: Addition has no effect on the number when it is 1e-16 or smaller




#TASK 5

def quadratic_solve(a,b,c):
    r = m.sqrt(b**2 - 4*a*c)
    return ((-b+r)/(2*a), (-b-r)/(2*a))

print("x =", quadratic_solve(0.001,1000,0.001))
            

def quadratic_solve_reexpressed(a,b,c):
    r = m.sqrt(b**2 - 4*a*c)
    return (2*c/(-b-r), 2*c/(-b+r)) #Simplified the given equation
print("x =", quadratic_solve_reexpressed(0.001,1000,0.001))


# In the first function, the first root is a bit wrong though the second one is correct. 
# This is because Python avoid subtracting nearly equal numbers. So when the term b^2 >> 4ac, this is very similar to computing -b + b.
# In the second function we switch the sign, hence the first root becomes correct and the second inaccurate.
# An improved method will therefor avoid this substraction by using the second expression to calculate the first root and the first expression to calculate the second root.


def quadratic_solve_improved(a,b,c):
    r = m.sqrt(b**2 - 4*a*c)
    return (2*c/(-b-r), (-b-r)/(2*a))
print("x =", quadratic_solve_improved(0.001,1000,0.001))




#TASK 6

def f(x):
    return x*(x-1)

def derivative(x, delta):
    return (f(x+delta)-f(x))/delta

print("Analytical solution: f'(x) = 2x-1  ")
print("Analytical: f'(5) = 9")
for i in range(-2,-15,-2):
    print(f"delta = 1e{i}: f'(5)= {derivative(5,10**(i))}. Deviation = {derivative(5,10**(i))-9} ")

#How does the accuracy scale with delta?
#More accurate for smaller delta, but decreases when delta becomes too small




#TASK 7


def integral(N):
    I = 0
    h = 2/N
    for k in range(1,N+1):
        x = -1 + 2*k/N
        y_k = m.sqrt(1-x**2)
        I += h*y_k
    return I

print(integral(100))



for i in range(3,8):
    print("I =",integral(10**i), "for N =", 10**i)
    get_ipython().run_line_magic('timeit', 'integral(10**i)')
    

#Result:

#I = 1.570743738501071
#647 µs ± 30.3 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
#I = 1.5707946637152914
#6.26 ms ± 218 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
#I = 1.5707962742034225
#61 ms ± 1.26 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
#I = 1.5707963251317272
#599 ms ± 9.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
#I = 1.5707963267423612
#6.01 s ± 45.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

#N can be increased up to approximately N = 1 000 000

# By running the loop above one can see that the maximum value of N before the code runs in over a second is approximately 1 000 000. 
# For values over this the changes in I is very small ~1e-10, so the gain of running it for a whole minute is small compared to a lot longer running time.
