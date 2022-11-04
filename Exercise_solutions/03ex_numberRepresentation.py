#!/usr/bin/env python
# coding: utf-8

# # Exercises 3: Number representation

# ### Tone Alsvik Finstad

# ### 1. Number representation
# 
# Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex). Determine the input type in the function, and pass another argument to choose the output representation.

# In[75]:


#Here I have assumed that binary numbers has only 0 and 1 etc, i.e that we don't have 0b in binary and 0x in hex. 
def converter(input_variable, output_type):
    if set(input_variable)=={"0","1"} or set(input_variable)=={"0"} or set(input_variable)=={"1"}:
        number=2
    else:
        try: 
            input_variable=str(int(float(input_variable)))
            number=10
        except:
            number=16
        
    if (output_type=="dec"):
        return float(int(input_variable, base=number))
    elif (output_type=="hex"):
        return hex(int(input_variable, base=number))
    else:
        return bin(int(input_variable, base=number))
    
    
    
#If I assume that binary starts with 0b and hex starts with 0x:
def converter_2(input_variable, output_type):
    if input_variable[:2]=="0b":
        number=2
        input_variable=input_variable[2:]
    elif input_variable[:2]=="0x":
        number=16
        input_variable=input_variable[2:]
    else:
        input_variable=str(int(float(input_variable)))
        number=10
        
    if (output_type=="dec"):
        return float(int(input_variable, base=number))
    elif (output_type=="hex"):
        return hex(int(input_variable, base=number))
    else:
        return bin(int(input_variable, base=number))
    
#Testing first method
a="1010101001"
b="0b2a5"
c="45733.0"
print(converter(a,"hex"))
print(converter(b,"bin"))
print(converter(b,"dec"))
print(converter("134.0", "hex"))

#Testing second method
print(converter_2("0b00110010101","hex"))
print(converter_2("0x61b27a","bin"))
print(converter_2("0x61b27a","dec"))
print(converter_2("134.0", "hex"))


# ### 2. 32-bit floating point number
# 
# Write a function that converts a 32 bit binary string (for example, 110000101011000000000000) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.
# 
# 
# ${\rm mantissa}=1.f=1+\frac{m_{n-1}}{2^{1}}+\frac{m_{n-2}}{2^{2}}+..+\frac{m_{0}}{2^{n}}$

# In[92]:


def calc_mantissa(num):
    mantissa=1
    for n in range(len(num)):
        mantissa+=float(num[n])/2**(n+1)
    return mantissa

    
def floating_point_to_decimal(string):
    return (-1)**(int(string[0]))*2**(int(string[1:9],base=2)-127)*(calc_mantissa(string[9:32]))


test="110000101011000000000000"
print(floating_point_to_decimal(test))


# ### 3. Underflow and overflow
# 
# Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your computer.
# 
# Hint: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.

# In[129]:


import numpy as np
a=1.0
b=1.0


while a<np.inf:
    max_val=a
    a*=2
print(f"Overflow limit: {max_val}")
    
#8.98846567431158e+307

while b>0:
    min_val=b
    b/=2
print(f"Underflow limit: {min_val}")
    
#5e-324
    


# ### 4. Machine precision
# 
# Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
# 
# Hint: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.

# In[131]:


a=float(1.0)
for i in range(100):
    b=a
    a+=10**-i
    diff=a-b
    if diff==0:
        print(f"Machine presicion: {10**-i}")
        break

#10^-16 


# ### 5. Quadratic solution
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

# In[105]:


#a)
def quad_solver(a,b,c):
    return ((-b+np.sqrt(b**2-4*a*c))/(2*a)),((-b-np.sqrt(b**2-4*a*c))/(2*a))

a=0.001
b=1000
c=0.001

print(quad_solver(a,b,c))


# The cardinal rule of numerical analysis says that you should avoid subtracting two nearly equal numbers. Here in the first solution we subtract b from $\sqrt{b^{2}-4ac}$ which for our numbers is very close. This causes the calculation to lose precision, causing a faulty solution. The second solution however is correct. 

# In[128]:


#b)
def quad_solver_2(a,b,c):
    return ((2*c))/((-b-np.sqrt(b**2-4*a*c))),((2*c))/((-b+np.sqrt(b**2-4*a*c)))

a=0.001
b=1000
c=0.001

print(quad_solver_2(a,b,c))


# In this case we are subtracting the same numbers as in a) in our second solution, causing us to loose precision. So in this case our first solution is fine, but second is faulty.

# In[107]:


#c) Want to make sure we never subtract two similar numbers:

def quad_solver_improved(a,b,c):
    return ((2*c))/((-b-np.sqrt(b**2-4*a*c))), ((-b-np.sqrt(b**2-4*a*c))/(2*a))

a=0.001
b=1000
c=0.001

print(quad_solver_improved(a,b,c))


# In the improved method I have only multiplied the numerator and the denominator by $-b\mp\sqrt{b^2-4ac}$ in the case with +, because this is where we could have subtraction of similar numbers, while the other solution is left untouched to not cause the same problem here. 

# ### 6. The derivative
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

# In[109]:


import matplotlib.pyplot as plt

def f(x):
    return x*(x-1)

#a)
def df(x,delta):
    return (f(x+delta)-f(x))/delta

def df_analytic(x):
    return (2*x-1)

print(df(1,10**(-2)))
print(df_analytic(1))


# In[125]:


#b)
print("Testing some values:")
print(f"Lambda=10^(-4) : {df(1,10**(-4))}")
print(f"Lambda=10^(-6) : {df(1,10**(-6))}")
print(f"Lambda=10^(-8) : {df(1,10**(-8))}")
print(f"Lambda=10^(-10) : {df(1,10**(-10))}")
print(f"Lambda=10^(-12) : {df(1,10**(-12))}")
print(f"Lambda=10^(-14) : {df(1,10**(-14))}")

#Decided to plot the error over decreasing delta-values to see a trend:
l=[]
num=[]
for i in range(4,15):
    l.append(df(1,10**(-i))-df_analytic(1))
    num.append(i)
plt.plot(num,l)
plt.title("Error as a function of decreasing delta-values")
plt.xlabel("Delta=10^(-x)")
plt.ylabel("Error")
plt.show()


# Can see that the error starts increasing again for $\delta$ smaller than $10^{-8}$, so the highest accuracy is for $\delta = 10^{-8}$.

# ### 7. Integral of a semicircle
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

# In[52]:


import numpy as np

def Riemann_sum(N):
    I=0
    for k in range(N):
        I+=(2/N)*np.sqrt(1-(-1+(2/N)*k)**2)
    return I


get_ipython().run_line_magic('timeit', 'I=Riemann_sum(250000)')


# **Tested for:**
# 
# 
# N=300000 --- 1.26 s ± 78.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
# 
# 
# N=250000 --- 980 ms ± 117 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
# 
# 
# N=200000  --- 809 ms ± 11.3 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
# 
# 
# N=100000  --- 424 ms ± 36.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
# 
# 
# N=10000  --- 39.3 ms ± 4.97 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
# 
# 
# N=1000  --- 5.01 ms ± 1.44 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 
# 
# N=100  --- 434 µs ± 65.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
# 
# 
# 
# 
# **Comment:**
# I see that we can increase N up to around 250000 and still have a runtime of under 1 second. Below I will check how this will affect the results.

# In[56]:


I_1=Riemann_sum(100)
print(f"Result with N=100: I={I_1}")
I_2=Riemann_sum(250000)
print(f"Result with N=250000: I={I_2}")

diff=I_2-I_1
print(f"Increasing N to 250000 from 100 makes the result {diff} closer to the analytical solution")

#Analytical: 1.57079632679


# In[127]:


import matplotlib.pyplot as plt
N_list=np.linspace(100,250000,100)
I_list=[]
analytical=[]
for N in N_list:
    I_list.append(Riemann_sum(int(N)))
    analytical.append(1.57079632679)
plt.plot(N_list,I_list, label="Riemann-sum")
plt.plot(N_list,analytical, label="Analytical")
plt.title("Sum as a function of N")
plt.legend()
plt.show()


N_list=np.linspace(100,2500,500)
I_list=[]
analytical=[]
for N in N_list:
    I_list.append(Riemann_sum(int(N)))
    analytical.append(1.57079632679)
plt.plot(N_list,I_list, label="Riemann-sum")
plt.plot(N_list,analytical, label="Analytical")
plt.title("Sum as a function of N")
plt.legend()
plt.show()


# I made the plots above to visualize the change in the sum as a function of N, and as you can see it converges to the analytical value very fast, and therefore I conclude that I would choose an N of around 1500 to make sure the value gas converged but without a very long runtime.  
