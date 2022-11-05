import sys
import math
import timeit
import numpy as np
"""
Exercise 1 : NUMBER REPRESENTATION
"""
print("Exercise 1 : NUMBER REPRESENTATION \n")

def number_representation(x,type):
    #0b : binary
    #0x : hexadecimal
    #nothing : decimal
    #we decompose the number to see if it is a binary, hexadecimal or decimal
    input_type = 0
    if isinstance(x,int):
        input_type = 1
    else:
        number = (list(x))
        #Only 1 number -> it is a decimal 
        if (number[1] == "b"):
            #input_type = 2 -> binary
            input_type = 2
        elif (number[1] == "x"):
            #input_type = 3 -> hexa
            input_type = 3

    if (type == "decimal"):
        if (input_type == 2): #-> binary
            return int(x, 2)
        elif (input_type == 3): #-> hexa
            return int(x,16)
    elif (type == "hexadecimal"):
        if (input_type == 2): #-> binary
            return hex(int(x, 2))
        else: 
            return hex(int(x))
    elif (type == "binary"):
        if (input_type == 3): #-> hexa
            return bin(int(x,16))
        else:
            return bin(int(x))
    else :
        print("ERROR : output convertion")

a = 23
print('decimal : ', a)
a_bin = bin(a)
print('binary : ', a_bin)
a_hex = hex(a)
print('hexadecimal : ', a_hex)
print('Decimal -> hexadecimal : ', a, '->',number_representation(23,"hexadecimal"))
print('hexadecimal -> decimal : ', a_hex, '->',number_representation(a_hex,"decimal"))
print('binary -> hexadecimal : ', a_bin, '->',number_representation(a_bin,"hexadecimal"))

"""
Exercise 2 : 32-BIT FLOATING POINT NUMBER
"""
print("\n Exercise 2 : 32-BIT FLOATING POINT NUMBER\n")
def floating_point_number(x):
    signe = 0
    #Check the sign
    if (x[0] == '0'):
        signe = 0
    elif (x[0] == '1'):
        signe = 1

    #we calculate the exponent
    exponent = int(x[1:9], 2)

    #we calculate the mantisse
    n = 1
    mant_cal = 1
    for i in x[9:]:
        if (i == '1'):
            mant_cal = mant_cal + 2**(-n)
        n+=1

    if signe == 0:
        return mant_cal * 2**(exponent - 127)
    else :
        return - mant_cal * 2**(exponent - 127)
         
number = "11000010101100000000000"
print(floating_point_number(number))

#exampl during class -> we should find -5.5
number2 = "110000001011"
print(floating_point_number(number2))


"""
Exercise 3 : UNDERFLOW AND OVERFLOW
"""
print("\n Exercise 3 : UNDERFLOW AND OVERFLOW\n")
def floating_numbers_sys():
    underflow = 1
    overflow = 1
    N = 1076
    M = 1024
    for i in range(N):
        underflow=underflow/2
        print("--------")
        print(i)
        print(underflow)
    for i in range(M):
        overflow=overflow*2
        print("--------")
        print(i)
        print(overflow)

print(sys.float_info.max)
print(sys.float_info.min)
floating_numbers_sys()
"""
We can see that the overflow limit occurs when i=1023, the maximum float is 8.98847e+307
The underflow limit occurs when i=1074, that minimum float is 4.94066e-324
"""

"""
Exercise 4 : MACHINE PRECISION
"""
print("\n Exercise 4 : MACHINE PRECISION\n")
def machine_precision():
    precision = 0
    eps = 1
    for i in range(400):
        precision = precision + eps
        eps /= 1.1
        print("--------")
        print(eps)
        print(precision)

print(sys.float_info.epsilon)
machine_precision()
"""
We can see that by additionning a number under 7.792376308032534e-16
the result does not change
"""

"""
Exercise 5 : QUADRATIC SOLUTION
"""
print("\n Exercise 5 : QUADRATIC SOLUTION\n")

def quadratic_solution(a,b,c):
    delta = b**2-4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(b**2-4*a*c))/2*a
        x2 = (-b - math.sqrt(b**2-4*a*c))/2*a
    elif delta == 0:
        x1 = -b/2*a
    else:
        print('no real root')
    return (x1,x2)

print(quadratic_solution(0.001, 1000, 0.001))
#Solution : (-9.999894245993345e-13, -0.999999999999)
#We find the wrong solution 
#Good solution : x1 = −9.99989E−7 x2 = −1000000

def quadratic_solution_b(a,b,c):
    x1_numerator = (-b + math.sqrt(b**2-4*a*c)) * (-b + math.sqrt(b**2-4*a*c))
    x2_numerator = (-b - math.sqrt(b**2-4*a*c)) * (-b - math.sqrt(b**2-4*a*c))
    x1_denominator = 2*a * (-b + math.sqrt(b**2-4*a*c))
    x2_denominator = 2*a * (-b - math.sqrt(b**2-4*a*c))
    x1 = x1_numerator/x1_denominator
    x2 = x2_numerator/x2_denominator
    return (x1,x2)

print(quadratic_solution_b(0.001, 1000, 0.001))


"""
But when I calculate the numerator and the denominator separtly , I do not find the same solution. Therefore, my system is not able to put the fraction in the decimal base. Therefore, the result that we find is not 
accurate. In the b), we avoid calculating nearly equal numbers and loosing precision when going from the decimal representation to the binary representation. 
"""

"""
To obtain more precise results with floating number, we need to avoid substacting nearly equal numbers. Indeed, 
the more similar two numbers are, the more precision we loose. 
Here, the problem is that b almost equal to math.sqrt(b**2 - 4*a*c)
Therefore, we need to multiply the result by its conjugate => using the Citardauq formulat (see quadractic_solution_b function)
"""

"""
Exercise 6 : THE DERIVATIVE
"""
print("\n Exercise 6 : THE DERIVATIVE\n")

#f'(x) = 2x - 1
def derivative(x, delta):
    def function(x):
        return x*(x-1)
    return ((function(x + delta) - function(x))/delta)

print(derivative(1, 10**-2))
"""
Analytically the derivative of the function at the point x = 1 is 2*1-1=1
We find 1.010000000000001 and not 1 because delta is not close enough to zero. Indeed, 
if we apply the definition, delta must tend to 0 to find the right result
"""

deltas = [10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14]
for i in deltas:
    print(derivative(1, i), '\t\t', i)

"""
We can see that by decreasing the delta, we approach a value of 1. 
However, when the delta is to small (starting from 1e-10), the system cannot compute it 
corretly. Therefore, the result are not precise and we have a derivative that start 
increasing and decreasing.
"""

"""
Exercise 7 : INTEGRAL OF A SEMICIRCLE
"""
print("\n Exercise 7 : INTEGRAL OF A SEMICIRCLE\n")


def Riemann(N):
    def semicircle(x):
        return math.sqrt(1-x**2)
    I = 0
    h = 2/N #the width of each slices
    x = np.linspace(-1, 1, N) #100 values for -1 to 1 (because the integral goes from -1 to 1)
    for k in range(1,N): #k from 1 to N
        #sum of h * function yk
        I = I + h*semicircle(x[k])
    return I

print(Riemann(100))


"""
The true value : 1.57079632679....
The value that we find : 1.5534179294048955
The value that we find is close to the true value. However, N needs to be bigger to 
be really close to the true value. Indeed, the N in the Riemann definition tends to the infinite
"""

N = 1
t = 0
#under 1 second : 
while t < 0.1:
    N_temp = N+100
    t_temp = timeit.timeit('Riemann(N)', globals=globals(), number=1)
    if t_temp > 0.1:
        break
    else:
        N=N_temp
        t=t_temp

print("N = ", N, "so that the computation run in ", t)
#N = 350001 so that the computation run in  0.09478401900014433

N = 1
t = 0
#under 1 minute : 
while t < 1:
    N_temp = N+10**5
    t_temp = timeit.timeit('Riemann(N)', globals=globals(), number=1)
    if t_temp > 1:
        break
    else:
        N=N_temp
        t=t_temp

print("N = ", N, "so that the computation run in ", t)
#N =  2700001 so that the computation run in  0.9048463549997905

#Let's see the gain in running it for 1 minutes
print("Running it in 1sec : ",Riemann(350001)) #1sec
print("Running it in 1min : ", Riemann(2700001)) #1min

#By running it for 1min, we calcule more N slices. By calculating more slices, the solution will be more precise