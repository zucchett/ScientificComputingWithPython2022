
from math import sqrt,pi
# You can solve these exercises in the room or at home. For this week, exercises have to be solved by creating a dedicated `.py` file (or files) called `03ex_numberRepresentation.py`.
# 
# In case you need multiple files, name them `03ex_numberRepresentation_es01.py`, `03ex_numberRepresentation_es02.py` and so on. In this case, it's convenient to create a dedicated directory, to be named `03ex_numberRepresentation`. 
# 
# The exercises need to run without errors with `python3`.


#Ex 1 ===================================================================================================================0
# 1\. **Number representation**
# 
# Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex).
# Determine the input type in the function, and pass another argument to choose the output representation.



def convto(number, tobase):
    '''
    accepts a binary, decimal or hexadecimal number and coverts it to the desired specified base
    '''
    try:
        if tobase == 10:
            if bin(int(number))[:2] == "0b": 
                return int(bin(number), 2)

            elif hex(number)[:2] == "0x":
                return int(number, 16)

    
        if tobase == 16:
            if str(number).isdigit():
                return hex(number)

            elif bin(number)[:2] == "0b":
                return hex(int(number, 2))


        if tobase == 2:
            if str(number).isdigit():
                return bin(number)

            elif hex(number)[:2] == "0x":
                return bin(number)
        else:
            return "bases can be: 2, 10 and 16"
    except:
        return "invalid value"

print(convto(0b1010, 16))



#Ex 2========================================================================================================================================================================
print("Ex 2 **32-bit floating point number**")
# 
# Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.


def convert(binum):
    '''
    accepts a 32 bit brinary string and converts it into a singular precision floating point in decimal representation'''
    s = binum[0]                             #sing bit
    esp = binum[1:9]                         #exponent bits
    mant = binum[9:]                         #fractional fart of the mantissa
    

    mantf= 0
    nn = 1
    for n in mant:
        mantf += int(n)/(2**nn)
    
        nn += 1
    mantf = 1 +mantf
    print( int(esp,2))
    p = int(esp, 2) -127
    return ((-1)**int(s)) * mantf * (2**p)



#Ex 3 ===============================================================================================================================================================0
print("Ex 3 **Underflow and overflow**")
# 
# Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your computer. 
# 
# *Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.



under = 1.0                                           #value to start checking underflow
over = 1.0                                            #value to start checking overfloe
under_count = 0
over_count = 0
countsnumbers= []
countsnumbers2 = []

while under != 0.0:                                     #return value of the underflow is 0.0
    countsnumbers.append((under_count, under))
    under/=2                                            #dividing the value by 2 every step of the loop
    under_count+=1                                      #count of the times we did the operation


while over < float("inf"):                              #return value of the overflow is inf
        countsnumbers2.append((over_count,over))       
        over *= 2                                       #dividing the value by 2 every step of the loop
        over_count+=1                                   #count of the times we did the operation
    
     
print(countsnumbers[-1],countsnumbers2[-1])

    


#Ex 4 ======================================================================================================================================================
print("Ex 4 **Machine precision**")
# 
# Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
# 
# *Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.


a = 1.0
b = 1.0
l=[]
while b!=0.0:
    b/=2
    a=a+b
    if a!=2.0:
        l.append(a)
print("machine precision:",2-(l[-1]))


#Ex 5 ============================================================================================================================================================================================
print("Ex 5 **Quadratic solution**")
# 
# Write a function that takes in input three parameters $a$, $b$ and $c$ and prints out the two solutions to the quadratic equation $ax^2+bx+c=0$ using the standard formula:
# $$
# x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
# $$
# 
# (a) use the function to compute the solution for $a=0.001$, $b=1000$ and $c=0.001$
# 
# (b) re-express the standard solution formula by multiplying the numerator and the denominator by $-b\mp\sqrt{b^2-4ac}$ and again find the solution for $a=0.001$, $b=1000$ and $c=0.001$. How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)
# 
# (c) write a function that computes the roots of a quadratic equation accurately in all cases



from math import sqrt


a = 0.001
b = 1000
c = 0.001


delta = sqrt((b**2) - (4*a*c))
results = [(-b + delta)/(2*a), (-b - delta)/(2*a) ] 
print(results)



results = [2*c/ (-b-delta),  2*c / (-b + delta) ]
print(results)

# the results change becouse of the round-off error: in this case se solution of x2 is more precise, while the x1 isn't



results = [((-b + delta) * (-b-delta)) / ((2*a) * (-b-delta)), 2*c / (-b + delta) ]
print(results)


#Ex 6 =====================================================================================================================================================================================
print("Ex 6 **The derivative**")
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


def func(x):
    return x*(x-1)

def der(x,delta):
    return (func(x+delta) -func(x))/delta




deltas = [(1/(10**n)) for n in range(4,15, 2)]

n =4
x = 1
for delta in deltas:
    deriv = der(x, delta)
    print(f", x :1, delta : 10^ -{n}, derivative: ", deriv)
    n += 2
    
#we can see:
# -- for delta != 10^-14 ,the algorithmic error is decreasing every step: we see indeed that the tendency of the result is the same
# -- for delta = 10^ -14, the tendency changes becouse of the round-off error: we loose precision, so the tendency changes


#Ex 7 =================================================================================================================================================
print("Ex 7 **Integral of a semicircle**")
# 
# Consider the integral of the semicircle of radius 1:
# $$
# I=\int_{-1}^{1} \sqrt(1-x^2) {\rm d}x
# $$
# which is known to be $I=\frac{\pi}{2}=1.57079632679...$.
# 
# Alternatively we can use the Riemann definition of the integral:
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




def integral(n):

    h = 2/n
    result = 0
    for i in range(0, n): 
        result += h * sqrt(1-(i/n)**2)

    return result

print(pi/2,integral(100))
#the values are different as a consequence of the approximation error present in the algorithm (the higher the N, the smaller becomes the approximation/algorithmic error needed).




# time < 1s : N between 8.320.000 and 8.330.000 (on my notebook)
#we gain 0.009412068637049797 of accuracy

print(integral(8300000))



# time almost 1 minute: N = 490000000 (on my notebook)
#we gain 0.0094121870539714 of accuracy
print(integral(490000000))



