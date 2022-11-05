#1-Number representation
def type_nr(nr):
    if str(nr)[:2] == "0b":
        return "bin"
    elif str(nr)[:2] == "0x":
        return "hex"
    else:
        return "dec"

def convert(nr, output):
    input = type_nr(nr)
    type_dict = {"bin": 2, "dec": 10, "hex": 16}

    if output == "dec":
        return int(str(nr), type_dict[input])
    elif output == "bin":
        return bin(int(str(nr), type_dict[input]))
    elif output == "hex":
        return hex(int(str(nr), type_dict[input]))

#Testing by getting a value from the user
nr = input("Enter a number: ")
output = input("Enter the output type you want: ")
print(convert(nr, output))

#2-32-bit floating point number
bin_str = input("Enter a value: ")
def convert_bin(bin_str):
    if len(bin_str)!=32:
        print("ERROR: The value is not a 32 bit binary string!")
        return None
    sign = int(bin_str[0], 2)
    exponent = int(bin_str[1:9], 2)

    frac_str = bin_str[9:]
    fraction = 0
    nr = 1
    for f in frac_str:
        fraction += int(f) * 2**(-nr)
        nr += 1
    return (-1)*sign * (1+fraction) * 2*(exponent-127)
print(convert_bin(bin_str))

#3-Underflow and overflow
import math

var1 = 1.0
while var1 < math.inf:
    max_val = var1
    var1 *= 2
print("Max value:", max_val)

var2 = 1.0
while var2 > 0:
    min_val = var2
    var2 /= 2
print("Min Value:", min_val)

#4-Machine precision
a = 1.0
b = 1.0
c = 0
while True:
    addition = 10**(-c)
    print(c, b+addition)
    if a == b+addition:
        print(f"As we can see by the results, the addition has no effect on the number when it is 1e-{c} or smaller.")
        break
    c+= 1

#5-Quadratic solution
#a)
def quadratic_sol(a,b,c):
    r = math.sqrt(b*b - 4*a*c)
    return ((-b+r)/(2*a), (-b-r)/(2*a))

print("xa =", quadratic_sol(0.001,1000,0.001))

#b)
def quadratic_re(a,b,c):
    r = math.sqrt(b*b - 4*a*c)
    return (2*c/(-b-r), 2*c/(-b+r))
print("xb =", quadratic_re(0.001,1000,0.001))

# The quadratic equation violated the cardinal rule of numerical analysis that says that # you have to avoid subtracting nearly equal numbers.
# This means that the more similar two numbers are, the more precision you can lose from subtracting them.

#c)

def quadratic_all(a,b,c):
    r = math.sqrt(b**2 - 4*a*c)
    return (2*c/(-b-r), (-b-r)/(2*a))
print("xc =", quadratic_all(0.001,1000,0.001))

#6-The derivative
#a)
def f(x):       
    return x*(x-1) #The function f(x) = x (x-1)

def der(x, delta):
    return (f(x+delta)-f(x))/delta  #Calculate the derivative

print("The derivative analytically :  1")
for i in range(-2, -15, -2):
    print(f"delta = 1e{i} ---> f'(1)= {der(1, 10**(i))}")   # x = 1

#b)
# We can see by the results that the smaller the delta is, the more accurate the program.


#7-Integral of a semicircle

#a)
def integral(N):
    I = 0
    h = 2/N
    for k in range(1, N+1):
        x = -1 + 2*k/N
        y_k = math.sqrt(1-x*x)
        I += h*y_k
    return I
print("The result when N = 100 is: ",integral(100))
for i in range(3, 10):
    print("The result is", integral(10*i), "when N =", 10*i)
    get_ipython().run_line_magic('timeit', 'integral(10**i)')   # measure the time


#b)
#The true value of the integral of the semicircle is not equal to the computed value by the program.
# N - is up to approximately N = 1 000 000.