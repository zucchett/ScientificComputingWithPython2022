import sys
import math
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
        else:
            input_type = 1

    if (type == "decimal"):
        if (input_type == 2): #-> binary
            return int(x, 2)
        elif (input_type == 3): #-> hexa
            return int(x,16)
    elif (type == "hexadecimal"):
        if (input_type == 2): #-> binary
            return hex(int(x, 2))
        elif (input_type == 1): #-> decimal
            return hex(int(x))
    elif (type == "binary"):
        if (input_type == 1): #-> decimal
            return bin(int(x))
        elif (input_type == 3): #-> hexa
            return bin(int(x,16))
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
    number = list(x)
    signe = 0
    #Check the sign
    if (number[0] == '0'):
        sign = 0
    elif (number[0] == '1'):
        signe = 1

    #we calculate the exponent
    l = list()
    l.append('0b')
    for i in number[1:9]:
        l.append(i)
    exp = (''.join(l))
    exponent = (int(exp, 2))

    #we calculate the mantisse
    m = list()
    n = 1
    mant_cal = 1
    for i in number [9:]:
        if (i == '1'):
            mant_cal = mant_cal + 2**(-n)
        n+=1

    if signe == 0:
        res = mant_cal * 2**(exponent - 127)
    else :
        res = - mant_cal * 2**(exponent - 127)

    return res
         
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
        print(i,'\t\t|',"%6e"%underflow)
    for i in range(M):
        overflow=overflow*2
        print(i,'\t\t|',"%6e"%overflow)

print(sys.float_info.max)
print(sys.float_info.min)
#floating_numbers_sys()
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
#machine_precision()
"""
We can see that by additionning a number under 7.792376308032534e-16
the result does not change
"""

"""
Exercise 5 : QUADRATIC SOLUTION
"""
print("\n Exercise 4 : QUADRATIC SOLUTION\n")

def quadratic_solution(a,b,c):
    x1 = (-b + math.sqrt(b**2-4*a*c))/2*a
    x2 = (-b - math.sqrt(b**2-4*a*c))/2*a
    return (x1,x2)

print(quadratic_solution(0.001, 1000, 0.001))
#Solution : (-9.999894245993345e-13, -0.999999999999)

def quadratic_solution_b(a,b,c):
    x1 = ((-b + math.sqrt(b**2-4*a*c))*(-b + math.sqrt(b**2-4*a*c)))/((2*a)*(-b + math.sqrt(b**2-4*a*c)))
    x2 = ((-b - math.sqrt(b**2-4*a*c))*(-b - math.sqrt(b**2-4*a*c)))/((2*a)*(-b - math.sqrt(b**2-4*a*c)))
    return (x1,x2)

print(quadratic_solution_b(0.001, 1000, 0.001))
#Solution : (-9.999894245993346e-07, -999999.999999)
"""
When we calculate $-b\mp\sqrt{b^2-4ac}$ we don't find the true result because we cannont represented in binary the 
fraction in the decimal base. That is why we don't have exacly the result attended and we find 2 differents results 
by multplying the numerator and denominator by the same fonction. The problem is the floating point precision that give 
slightly wrong results
"""

def roots_quadratiq_solution(a,b,c):
    return (-b + math.sqrt(b**2-4*a*c), -b - math.sqrt(b**2-4*a*c))
print(roots_quadratiq_solution(0.001,1000,0.001))
