# ********** Question 1 **********
import math
import timeit

print("Question 1")
import math

# The user must enter hexadecimal number starting with '0x' and binary numbers with '0b'
# convertion type d stands for decimal, b for binary, x for hexadecimal. Enter just b, d or x

def convertNumber(og_num, og_type, con_type):
    if og_type == 'd':
        if con_type == 'x':
            return hex(int(og_num))
        elif con_type == 'b':
            return bin(int(og_num))
        else:
            return og_num
    elif og_type == 'b':
        if con_type == 'd':
            return int(og_num,2)
        elif con_type == 'x':
            return hex(int(og_num, 2))
        else:
            return og_num
    else:
        if con_type == 'b':
            return bin(int(og_num, 16))
        elif con_type == 'd':
            return int(og_num, 16)
        else:
            return og_num

og_num = input("Enter the number to be converted: ")
og_type = 'd'
if og_num.startswith('0b'):
    og_type = 'b'
elif og_num.startswith('0x'):
    og_type = 'x'
con_type = input("Enter the type that the number will be converted to (d, b, x): ")
result = convertNumber(og_num, og_type, con_type)

print(result)

# ********** Question 2 **********
print("Question 2")
def convertToInt(mantissa_str):
    power_count = -1
    mantissa_int = 0
    for i in mantissa_str: # computes the mantissa based on the bits
        mantissa_int += (int(i) * pow(2, power_count))
        power_count -= 1
         
    return (mantissa_int + 1)


def converter(ieee_32):
    # Seperate the bits according to the IEEE754 standart
    sign_bit = int(ieee_32[0])
    exponent_bias = int(ieee_32[1 : 9], 2)
    exponent_unbias = exponent_bias - 127
    mantissa_str = ieee_32[9 : ]
 
    mantissa_int = convertToInt(mantissa_str)

    # finds the summation of the values based on their position and value
    real_no = pow(-1, sign_bit) * mantissa_int * pow(2, exponent_unbias)
    return real_no

number = '110000101011000000000000'
decimal_number = converter(number)
print("The float value:",decimal_number)


# ********** Question 3 **********
print("Question 3")
over = []
over_count = 0
var_1 = 1
while True:
    over_count += 1
    var_1 *= 2
    try: # adds new elements until it cathces and error. that point is the overflow limit
        over.append("%.5e"%var_1)
    except:
        print( "overflow count: ", over_count-2)
        print( "overflow: ", over[over_count-2])
        break

under = []
under_count = 0  
var_2 = 1
while True:
    under_count += 1
    var_2 /= 2
    under.append(var_2)
    if(under[under_count-1] == 0): # finds increasingly smaller numbers until they are insignificant and counted as 0
        print( "underflow count: ", under_count-2)
        print( "underflow: ", under[under_count-2])
        break


# ********** Question 4 **********
print("Question 4")
var_1 = 1
check = 0
var_list = []

count = 0
while True:
    check = var_1 * (2** (-count)) # adds increasingly smaller numbers until it is insignificant
    var_list.append(check)
    if(check == 0):
        print("last number: ", var_list[count - 1] , " last step: ", count)
        break
    var_1 = check
    count += 1


# ********** Question 5 **********
print("Question 5")
import math

# x values based on the formula
def quadraticEquation(a,b,c):
    x_1 = (math.sqrt(b**2 - (4 * a * c)) - b) / (2 * a)
    x_2 = (- math.sqrt(b**2 -( 4 * a * c)) - b) / (2 * a)
    return x_1, x_2

# x values after the multiplications
def quadraticEquationModified(a,b,c):
    temp_neg = (- math.sqrt(b**2 - (4 * a * c)) - b)
    temp_pos = (math.sqrt(b**2 - (4 * a * c)) - b)
    x_1 = (temp_neg * temp_neg) / ((2*a) * temp_neg)
    x_2 = (temp_pos * temp_pos) / ((2*a) * temp_pos)
    x_3 = (temp_neg * temp_pos) / ((2*a) * temp_pos)
    x_4 = (temp_pos * temp_neg) / ((2*a) * temp_neg)
    return x_1, x_2, x_3, x_4

def accurate(a,b,c):
    delta = b**2 - (4 * a * c)
    x_1 = 0
    x_2 = 0
    if(delta == 0): # checks the value of delta based on its sign
        x_1 = -b / (2*a)
        x_2 = -b / (2*a)
        return x_1, x_2
    elif(delta != 0):
        x_1 = (math.sqrt(delta) - b) / (2 * a)
        x_2 = (- math.sqrt(delta) - b) / (2 * a)
        return x_1, x_2
    else:
        reel_p =  (- b) / (2 * a) # if delta is smaller than 0, find also the imaginary root
        im_p = math.sqrt(abs(delta)) / (2 * a)
        reel_x = reel_p, '+', im_p, 'i'
        im_x = reel_p, '-', im_p, 'i'
        return reel_x, im_x

a = 0.001
b = 1000
c = 0.001
print("part a")
sol_1, sol_2 = quadraticEquation(a,b,c)
print(sol_1)
print(sol_2)
print("part b")
sol_mod_1, sol_mod_2, sol_mod_3, sol_mod_4 = quadraticEquationModified(a,b,c)
print(sol_mod_1)
print(sol_mod_2)
print(sol_mod_3)
print(sol_mod_4)
print("part c")
sol_acc_1, sol_acc_2 = accurate(a,b,c)
print(sol_acc_1)
print(sol_acc_2)

# Test to check delta
a = 1
b = -2
c = 1
sol_acc_1, sol_acc_2 = accurate(a,b,c)
print(sol_acc_1)
print(sol_acc_2)


# ********** Question 6 **********
print("Question 6")
def func(x):
    return x*(x-1)

# function that gives the derivative based on the formula
def derivative(x, t):
    result = (func(x + t) - func(x)) / t
    return result

x = 1
t_1 = 10**-2
t_2 = 10**-4
t_3 = 10**-6
t_4 = 10**-8
t_5 = 10**-10
t_6 = 10**-12
t_7 = 10**-14

print('x: ', x)
print('result for', t_1, ': ',derivative(x,t_1))
print('result for', t_2, ': ',derivative(x,t_2))
print('result for', t_3, ': ',derivative(x,t_3))
print('result for', t_4, ': ',derivative(x,t_4))
print('result for', t_5, ': ',derivative(x,t_5))
print('result for', t_6, ': ',derivative(x,t_6))
print('result for', t_7, ': ',derivative(x,t_7))
# At first, as the delta gets smaller, it gets closer to 0. Therefore the derivative gets closer to the theoritical value
# After 10**-8, the result gets further away from the theoritical.


# ********** Question 7 **********

print("Question 7")
import math
import timeit

# Performs the function based on riemann definition of integral
def riemann(N):
    result = 0
    for i in range(1,N):
        h =  2 / N
        x = (h * i) - 1
        result += h * (math.sqrt( 1 - x**2 ))
    return result

result = riemann(100)
print("for N = 100: ")
print("result: ", result, "error: ", (math.pi/2) - result) # find the error based on the difference with pi/2


starttime = timeit.default_timer()
print("The start time is :",starttime)

result = riemann(14000000)
print("for N = 140000000: ")
print("Error: ", result, "Result: ", (math.pi/2) - result)

print("The time difference is :", timeit.default_timer() - starttime)

# As N increases, the result becomes more and more accurate. So running it for longer gives more accurate result
# For this example N= 140000000 gives a runtime close to one minute and the result is much more accurate than N=100