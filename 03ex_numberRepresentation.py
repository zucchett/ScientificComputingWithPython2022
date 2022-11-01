#Anaïs Fragne

#1. Number representation

def convert(x, output):#put 2,16,10 in output if you want a binary, hexadecimal or decimal conversion
    result =x
    if output==2:
        result = bin(x)
    if output==16:
        result = hex(x)
    if output == 10:
        for i in str(x):
            if i not in ("0","1"):#hexa
                break
            result = int(str(x), 16)
        result = int(str(x),2)
    return result


print(convert(11011,10))

#2. 32-bit floating point number


def floating_point(x):
    e= x[1:9]
    e=int(str(e),2)-127    
    n=-1
    mantisse=0
    for i in x[9:]:
        mantisse+=int(i)*2**(n)
        n-=1
    mantissa=1+mantisse
    if x[0]=='0':
        result = (2**e)*mantissa
    else:
        result = -(2**e)*mantissa
    return result

print(floating_point('110000101011000000000000'))
#print(floating_point('00111111010000000000000000000000')) 

#3. Underflow and overflow
underflow=1
overflow=1
N=1080
for i in range(N):
    underflow=underflow/2
    
    print(i,'\t\t','underflow: ',"%2.5e"%underflow)
for j in range(N):
    overflow=overflow*2
    print(j,'\t\t','overflow: ',"%2.5e"%overflow)

# We remark an error from i=1074 for the underflow and j=1023 for the overflow that means that these are the limits for my computer.

import sys
print(sys.float_info)

#4. Machine precision

for i in range(20):
    f=1.+10**(-(i+1))
    print(i+1,'\t\t',f)
# I remarked that as 10^16, the addition has no effects on the number

#5. Quadratic solution
import numpy as np
def quadra(a,b,c):
    delta= b**2-4*a*c
    x=()
    if delta>0:
        x=x+((-b-np.sqrt(delta))/2*a,)
        x=x+((-b+np.sqrt(delta))/2*a,)
        #x=x+(((-b-np.sqrt(delta))/2*a)*(-b-np.sqrt(delta))/(-b-np.sqrt(delta)),)
        #x=x+(((-b+np.sqrt(delta))/2*a)*(-b+np.sqrt(delta))/(-b+np.sqrt(delta)),)
    elif delta==0:
        x=x+(-b/2*a,)
    else:
        print('no real solutions')
    return x

print(quadra(0.001,1000,0.001))

#We obtained the same value with the two methods. That means that my computer is enough strong to compute those small numbers and it still have effects on the number

#6. The derivative
def func(x):
    return x*(x-1)

delta=10**(-2)
x=1
der=(func(x+delta)-func(x))/delta
print(der)

#Analytically: f'(x=1)=2*1-1=1
#"1" is different from "der=1.010000000000001" 
#This is due to the fact that delta has to be really close to 0 to be equal to 1, but it's impossible to reach this value for delta, that's why we have an approximation of 1


deltas=[10^-4,10^-6,10^-8,10^-10,10^-12,10^-14]
for d in deltas:
    print('d=',d,'\t\t','der= ',der)
#Always the same value because the addition with delta cannot be done because delta is too small for my computer
#That means that it's impossible to see the limit almost equal to 1 because the computer doesn't allow to compute so small numbers

#7. Integral of a semicircle
import numpy as np
def semi_circle(x):
    return np.sqrt(1-x**2)

def riemann(N,f):
    a = -1
    b = 1
    h = (b - a) / N
    x=np.linspace(a, b, N)
    sum=0
    for i in range(N-1):
        sum+=h*f(x[i])
    return sum

N=100
r=riemann(N,semi_circle)
print('Riemann: ',r)
#1.5534179

#a. 
# #The true value is pi/2 =1.5707963
print('pi/2= ',np.pi/2)
print("The difference between the two values is: ", abs(abs(r)-(np.pi/2)))

#b. 
import timeit
t=timeit.timeit('riemann(N,semi_circle)', globals=globals(), number = 1000)
temp=t/1000

while temp<1:
    N_new=N*10
    t_new=timeit.timeit('riemann(N_new,semi_circle)', globals=globals(), number = 1)
    temp=t_new/1
    if not temp <1:
        break
    else:
        N=N_new
        t=t_new

print("With N= ", N, ", the computation runs for: ", t, " seconds.")