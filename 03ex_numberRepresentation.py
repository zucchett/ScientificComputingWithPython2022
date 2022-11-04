# Exercise 1 - Number representation
print("Exercise 1")

def find_input_type(number):
    if str(number)[:2] == "0b":
        return "bin"
    elif str(number)[:2] == "0x":
        return "hex"
    else:
        return "dec"

def convert_rep(number, output_type):
    input_type = find_input_type(number)
    type_dict = {"bin": 2, "dec": 10, "hex": 16}

    if output_type == "dec":
        return int(str(number), type_dict[input_type])
    elif output_type == "bin":
        return bin(int(str(number), type_dict[input_type]))
    elif output_type == "hex":
        return hex(int(str(number), type_dict[input_type]))

# Testing
number = input("Please enter your number: ")
output_type = input("Please enter the output type you want: ")
print(convert_rep(number, output_type))

# Exercise 2 - 32-bit floating point number
print("\n")
print("Exercise 2")
bin_str = input("Please enter your input: ")
def convert_bin(bin_str):
    if len(bin_str)!=32:
        print("ERROR: Not a 32 bit binary string")
        return None
    sign = int(bin_str[0], 2)
    exponent = int(bin_str[1:9], 2)

    fraction_str = bin_str[9:]
    fraction = 0
    nr = 1
    for f in fraction_str:
        fraction += int(f) * 2**(-nr)
        nr += 1

    return (-1)**sign * (1+fraction) * 2**(exponent-127)

print(convert_bin(bin_str))

# Exercise 3 - Underflow and overflow
print("\n")
print("Exercise 3")

import math

variable1 = 1.0
while variable1 < math.inf:
    max_val = variable1
    variable1 *= 2
print(" ", max_val)

variable2 = 1.0
while variable2 > 0:
    min_val = variable2
    variable2 /= 2
print(" ", min_val)

# Exercise 4 - Machine precision

print("\n")
print("Exercise 4")
a2 = 1.0
b2 = 1.0
k2 = 0
while True:
    addition = 10**(-k2)
    print(k2, b2+addition)
    if a2 == b2+addition:
        print(f"Result: Addition has no effect on the number when it is 1e-{k2} or smaller")
        break
    k2 += 1

# Exercise 5 - Quadratic solution
print("\n")
print("Exercise 5")

def quadratic_solve(a,b,c):
    r = math.sqrt(b*b - 4*a*c)
    return ((-b+r)/(2*a), (-b-r)/(2*a))

print("x =", quadratic_solve(0.001,1000,0.001))

def quadratic_solve_reexpressed(a,b,c):
    r = math.sqrt(b*b - 4*a*c)
    return (2*c/(-b-r), 2*c/(-b+r))
print("x =", quadratic_solve_reexpressed(0.001,1000,0.001))

# The quadratic equation violated the cardinal rule of numerical analysis: avoid subtracting nearly equal numbers.
# The more similar two numbers are, the more precision you can lose from subtracting them.

# c

def quadratic_solve_improved(a,b,c):
    r = math.sqrt(b**2 - 4*a*c)
    return (2*c/(-b-r), (-b-r)/(2*a))
print("x =", quadratic_solve_improved(0.001,1000,0.001))

# Exercise 6 - The derivative

print("\n")
print("Exercise 6")
def f(x):       # Implementing the function f(x) = x (x-1)
    return x*(x-1)

def derivative(x, delta):  # Calculate the derivative
    return (f(x+delta)-f(x))/delta

print("Analytically:  1")   # Analytically
for i in range(-2, -15, -2):  # calculation for delta = 10ˆ(-4), 10ˆ(-6), 10ˆ(-8), 10ˆ(-10), 10ˆ(12), 10ˆ(-14)
    print(f"delta = 1e{i} ---> f'(1)= {derivative(1, 10**(i))}")   # x = 1

# b
# the smaller the delta, the more accurate the program.

# Exercise 7 - Integral of a semicircle
print("\n")
print("Exercise 7")
def integral_semicircle(N):
    I = 0
    h = 2/N
    for k in range(1, N+1):
        x = -1 + 2*k/N
        y_k = math.sqrt(1-x*x)
        I += h*y_k
    return I
print("The result when N = 100 is ",integral_semicircle(100)) # N = 100
print("\n")
for i in range(3, 10):
    print("The result is", integral_semicircle(10**i), "when N =", 10**i)
    get_ipython().run_line_magic('timeit', 'integral(10**i)')   # measure the time

# The computed value by the program is not equal to the true value of the integral of the semicircle.

# N - up to approximately N = 1 000 000






