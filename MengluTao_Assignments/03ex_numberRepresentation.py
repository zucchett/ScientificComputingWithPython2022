# %% [markdown]
# You can solve these exercises in the room or at home. For this week, exercises have to be solved by creating a dedicated `.py` file (or files) called `03ex_numberRepresentation.py`.
# 
# In case you need multiple files, name them `03ex_numberRepresentation_es01.py`, `03ex_numberRepresentation_es02.py` and so on. In this case, it's convenient to create a dedicated directory, to be named `03ex_numberRepresentation`.
# 
# The exercises need to run without errors with `python3`.
# 

# %% [markdown]
# 1\. **Number representation**
# 
# Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex).
# Determine the input type in the function, and pass another argument to choose the output representation.
# 

# %%
from nis import match
import math

def convert_bin_dec_hex(num,output_type):
    num_str = str(num)
    signal = num_str[:2]
    if signal.isdigit():
        signal = '1'
    match signal:
        case '0b': 
            match output_type:
                case 'bin':  print('This is a Binary number: ', num_str),
                case 'dec':  print('This is a Binary number, now converted into Decimal: ', int(num_str, 2)),
                case 'hex':  print('This is a Binary number, now converted into Hexadecimal: ', hex(int(num_str, 2))),
        case '1':
            match output_type:
                case 'bin':  print('This is a Decimal number, now converted into Binary: ', bin(int(num_str, 10))),
                case 'dec':  print('This is a Decimal number: ', int(num_str, 10)),
                case 'hex':  print('This is a Decimal number, now converted into Hexadecimal: ', hex(int(num_str,10))),
        case '0x':
            match output_type:
                 case 'bin': print('This is a Hexadecimal number, now converted into Binary: ', bin(int(num_str, 16))),
                 case 'dec': print('This is a Hexadecimal number, now converted into Decimal: ', int(num_str, 16)),
                 case 'hex': print('This is a Hexadecimal number: ', num_str)

#convert_bin_dec_hex('0b1010','dec')



# %% [markdown]
# 2\. **32-bit floating point number**
# 
# Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.
# 

# %%
def mantissaInt(mantissa_str):
 
    # variable to make a count
    # of negative power of 2.
    power_count = -1
 
    # variable to store
    # float value of mantissa.
    mantissa_int = 0
 
    # Iterations through binary
    # Number. Standard form of
    # Mantissa is 1.M so we have
    # 0.M therefore we are taking
    # negative powers on 2 for
    # conversion.
    for i in mantissa_str:
 
        # Adding converted value of
        # Binary bits in every
        # iteration to float mantissa.
        mantissa_int += (int(i) * pow(2, power_count))
 
        # count will decrease by 1
        # as we move toward right.
        power_count -= 1
         
    # returning mantissa in 1.M form.
    return (mantissa_int + 1)
 
def convert(binary_str):
    # Floating Point Representation
    # to be converted into real
    # value.
    binary_str = binary_str
    # First bit will be sign bit.
    sign_bit = int(binary_str[0])
    #print("sign_bit: ", sign_bit)
 
    # Next 8 bits will be
    # Exponent Bits in Biased
    # form.
    exponent_bias = int(binary_str[1 : 9], 2) 
    #print("exponent_bias: ", exponent_bias)

 
    # In 32 Bit format bias
    # value is 127 so to have
    # unbiased exponent
    # subtract 127.
    exponent_unbias = exponent_bias - 127
    #print("exponent_unbias: ", exponent_unbias)
 
    # Next 23 Bits will be
    # Mantissa (1.M format)
    mantissa_str = binary_str[9 : ]
    #print("mantissa_str: ", mantissa_str)
 
    # Function call to convert
    # 23 binary bits into
    # 1.M real no. form
    mantissa_int = mantissaInt(mantissa_str)
    #print("mantissa_int: ", mantissa_int)
 
    # The final real no. obtained
    # by sign bit, mantissa and
    # Exponent.
    real_no = pow(-1, sign_bit) * mantissa_int * pow(2, exponent_unbias)
 
    # Printing the obtained
    # Real value of floating
    # Point Representation.
    print("The float value of the given IEEE-755 representation is :",real_no)
    return real_no

#convert('00000011111000000000000000000000')
#convert('110000101011000000000000')




# %% [markdown]
# 3\. **Underflow and overflow**
# 
# Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your computer.
# 
# _Hint_: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.
# 

# %%
def flow(N):
    underflow = 1
    overflow = 1
    #print("|n ","\t\t" , "|  Underflow ","\t\t" ,"|  Overflow  |" )
    for i in range(1,N):
        underflow = underflow/2
        overflow = overflow*2
        print("|%2d"%i, "\t\t" , "|  %2.3e"%underflow, "\t\t" ,"|  %2.3e"%overflow, " |" )
        if(underflow == 0):
            print("underflow = ", underflow)
            break
        
    
#flow(5000)
    

# %% [markdown]
# 4\. **Machine precision**
# 
# Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
# 
# _Hint_: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.
# 

# %%
def machine_precision():
    # initializing value
    a = 2
    # initializing precision
    precision = 1
    # loop to find precision
    print("Executing...")
    while (a + precision) != a:      
        precision = precision / 1.00001
        # printing the precision
        #print("a=",a)

    print("Machine precision is : ", precision)

#machine_precision()

# %% [markdown]
# 5\. **Quadratic solution**
# 
# Write a function that takes in input three parameters $a$, $b$ and $c$ and prints out the two solutions to the quadratic equation $ax^2+bx+c=0$ using the standard formula:
# 
# $$
# x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
# $$
# 
# (a) use the function to compute the solution for $a=0.001$, $b=1000$ and $c=0.001$
# 
# (b) re-express the standard solution formula by multiplying the numerator and the denominator by $-b\mp\sqrt{b^2-4ac}$ and again find the solution for $a=0.001$, $b=1000$ and $c=0.001$. How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)
# 
# (c) write a function that computes the roots of a quadratic equation accurately in all cases
# 

# %%
import math,cmath

#(a)
def quadratic(a,b,c):
    d = (b**2) - (4*a*c)
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)
    print('The solution are {0} and {1}'.format(sol1,sol2))
#quadratic(0.001,1000,0.001)

#(b)
def quadratic2(a,b,c):
    d = (b**2) - (4*a*c)
    sol1 = ((-b-math.sqrt(d))*(-b+math.sqrt(d)))/((2*a) * (-b+math.sqrt(d)))
    sol2 = ((-b+math.sqrt(d))*(-b-math.sqrt(d)))/((2*a) * (-b-math.sqrt(d)))
    print('The solution are {0} and {1}'.format(sol1,sol2))
#quadratic2(0.001,1000,0.001)

def quadratic3(a,b,c):
    d = (b**2) - (4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print('The solution are {0} and {1}'.format(sol1,sol2))

#quadratic3(0.001,1000,0.001)

# %% [markdown]
# 6\. **The derivative**
# 
# Write a program that implements the function $f(x)=x(x−1)$
# 
# (a) Calculate the derivative of the function at the point $x = 1$ using the derivative definition:
# 
# $$
# \frac{{\rm d}f}{{\rm d}x} = \lim_{\delta\to0} \frac{f(x+\delta)-f(x)}{\delta}
# $$
# 
# with $\delta = 10^{−2}$. Calculate the true value of the same derivative analytically and compare it with the answer your program gives. The two will not agree perfectly. Why?
# 
# (b) Repeat the calculation for $\delta = 10^{−4}, 10^{−6}, 10^{−8}, 10^{−10}, 10^{−12}$ and $10^{−14}$. How does the accuracy scale with $\delta$?
# 

# %%
#import numpy as np

def f(x):
    x = x*(x-1)
    return x
#function(1)

#(a)
def derivative(x,m):
    m = math.pow(10, m)
    result = (f(x+m) - f(x))/m
    print("function2 value: ", result, "with m equals to: ", m)
    return result
#function2(1,-2)


#(b)
# function2(1,-4)
# function2(1,-6)
# function2(1,-8)
# function2(1,-10)
# function2(1,-12)
# function2(1,-14)






# %% [markdown]
# 7\. **Integral of a semicircle**
# 
# Consider the integral of the semicircle of radius 1:
# 
# $$
# I=\int_{-1}^{1} \sqrt(1-x^2) {\rm d}x
# $$
# 
# which is known to be $I=\frac{\pi}{2}=1.57079632679...$.
# 
# Alternatively we can use the Riemann definition of the integral:
# 
# $$
# I=\lim_{N\to\infty} \sum_{k=1}^{N} h y_k
# $$
# 
# with $h=2/N$ the width of each of the $N$ slices the domain is divided into and where
# $y_k$ is the value of the function at the $k-$th slice.
# 
# (a) Write a program to compute the integral with $N=100$. How does the result compare to the true value?
# 
# (b) How much can $N$ be increased if the computation needs to be run in less than a second? What is the gain in running it for 1 minute? Use `timeit` to measure the time.
# 

# %%
import math
def d(x):
    d = math.sqrt(1-(math.pow(x,2)))
    #print("d: ", d)
    return d
def sum(N):
    sum = 0
    h = 2/N # h = 0.5
    for i in range(N):
        sum = sum + h * d(-1+ i*h) 
    #print("function2 value: ", sum)
    return sum






#function2(100000000)


while (True):
    print('---- Menu for exercise 3 ----')
    print('Select the exercise you want to run:')
    print('1. Exercise 1')
    print('2. Exercise 2 ')
    print('3. Exercise 3')
    print('4. Exercise 4')
    print('5. Exercise 5')
    print('6. Exercise 6')
    print('7. Exercise 7')
    
    print('0. Exit')
    op = input("=> ")
    if op == '1':    
        convert_bin_dec_hex('0b1010','dec')
        
    elif op == '2':
        convert('110000101011000000000000')
        
    elif op == '3':

        try:
            flow(5000)
        except Exception as e:
            print('Exception: ', str(e))
        
  
        
    elif op == '4':
        machine_precision()
       
    elif op == '5':
        print('Select the exercise you want to run:')
        print('a. Exercise 5a')
        print('b. Exercise 5b')
        print('c. Exercise 5c')
        op2 = input("=> ")
        if op2 == 'a':
            quadratic(0.001,1000,0.001)
        elif op2 == 'b':
            quadratic2(0.001,1000,0.001)
            #Answer to 5b#
            #This solution is less precise than the previous one, because of the floating point error that is propagated when making the calculation.
        elif op2 == 'c':
            quadratic3(0.001,1000,0.001)
        
    elif op == '6':
        print('Select the exercise you want to run:')
        print('a. Exercise 6a')
        print('b. Exercise 6b')
        op2 = input("=> ")
        if op2 == 'a':
            derivative(1,-2)
        elif op2 == 'b':
            derivative(1,-4)
            derivative(1,-6)
            derivative(1,-8)
            derivative(1,-10)
            derivative(1,-12)
            derivative(1,-14)
            print("------Answer to 6b------")
            print("The accuracy is the best when delta is 10^-8, and it is the worst when delta is 10^-14, probably because of the floating point error")
    elif op == '7':
        print('Select the exercise you want to run:')
        print('a. Exercise 7a')
        print('b. Exercise 7b')
        op2 = input("=> ")
        if op2 == 'a':
            print("Using Riemann definition with N = 100 pieces, the integral is :",sum(100))
            print("The true value of the integral is: ", math.pi/2)
            print("------------ Anwser to 7a ------------")
            print("The result is not the same as the true value of the integral because the Riemann definition of the integral is an approximation of the integral and since the N = 100, it's a small number so the result is not that precise.")

        elif op2 == 'b':
            import timeit
            start = timeit.default_timer()
            print("Using Riemann definition with N = 2000000 pieces, the integral is :",sum(2000000))
            stop = timeit.default_timer()
            print('Time: ', stop - start)

            print("------------ Anwser to 7b ------------")
            print("With N equals to 2000000, the execution finishes in around one second. The bigger the N, the more precise the result will be. The gain in running it for 1 minute is that the result will be more precise.")

       
    elif op == '0':
        break


    input("\nPress Enter to continue...")

