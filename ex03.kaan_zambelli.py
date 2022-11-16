"""
Ex03 Kaan Zambelli 
"""

"""
Q1 Answer
"""
def RepresentConverter(sin,stype):
    if sin[0:2] == '0x': #hexadecimal
        if stype == "decimal":
            return int(sin,16)
        elif stype == "hexadecimal":
            return sin
        else:
            return bin(int(sin,16))
    else:
        if sin[0:2] == '0b': #binary
            if stype == "decimal":
                return int(sin,2)
            elif stype == "hexadecimal":
                return hex(int(sin,2))
            else:
                return sin
        else:
            if stype == "decimal":
                return int(sin)
            elif stype == "hexadecimal":
                return hex(int(sin))
            else:
                return bin(int(sin))
            
sin = input("Enter the value: ")
stype = input("Enter the output type as decimal/hexadecimal/binary")
RepresentConverter(sin,stype)

"""
Q2 Answer
"""

"""
Q3 Answer
"""
a = 1
b = 1
c = 2
try:
    for i in range(1500):
        a = a * 2
        print(i, "\t", "%2.5e"%a, "\t" , "overflow")
except:
    print("You are at the limit in the index ", "%2.5e"%i, "with the value ", "%2.5e"%a) 

a = 1
b = 1
c = 2
try:
    for i in range(1500):
        a = a / 2
        print(i, "\t", "%2.5e"%a, "\t" , "overflow")
        if "%2.5e"%a == 0.00000e+00:
            print("Underflow limit will start from the index",i)
            break
except:
    print("You are at the limit in the index ", "%2.5e"%i, "with the value ", "%2.5e"%a) 
    
"""
Q4 Answer
"""
num = 4
adder = 2

for i in range(70):
    num += adder
    adder = adder / 2
    print(i,"th index ", num, " the resultant number", adder, " and the adder value")

"""
Q5 - (a) Answer
"""

import math as m
def Quad(a,b,c):
    delta = b**2 - 4*a*c
    x = (-b - m.sqrt(delta)) / (2*a)
    y = (-b + m.sqrt(delta)) / (2*a)
    return x,y

x,y = Quad(0.001,1000,0.001)
print("First quadrant is: ", x , " and the second quadrant is: ", y)

"""
Q5 - (b) Answer
"""

def QuadMod(a,b,c):
    delta = b**2 - 4*a*c
    aa = (-b - m.sqrt(delta))
    bb = (-b + m.sqrt(delta))
    a = aa * aa / ((2*a)*aa)
    b = aa * bb / ((2*a*bb))
    c = bb * aa / ((2*a)*aa)
    d = bb * bb / ((2*a)*bb)
    return a,b,c,d

a,b,c,d = QuadMod(0.001,1000,0.001)
print("Prev x is: ",x,"new x's are", a," and",b)
print("Prev y is: ",y,"new x's are", c," and",d)

#Three of the values remain the same however we obtained a slight change in the case of
#quadrant multiplication of the quadrant with '-' sign with '+' sign
#The reason is that the approximation in the calculation in order to calculate the given operation
#That is why it seems that in the given operation it is rounding up the values during the calculation
#So it is the reason for we obtaining a completely different value where we expect the exact value

"""
Q5 - (c) Answer
"""
def QuadrantFuncCalc(a,b,c):
    delta = b**2 - 4*a*c
    
    if delta == 0:
        print(-b/(2*a))
    elif delta > 0:
        x,y = Quad(0.001,1000,0.001)
        print(x)
        print(y)
    else:
        print(-b/(2*a), "+", delta,"i")
        print(-b/(2*a), "-", delta,"i")

QuadrantFuncCalc(0.001,1000,0.001)

"""
Q6 - (a) Answer
"""

x = 1
s = 10**-2
#function is x*(x-1)
integ = (((x+s)*((x+s)-1)) - (x*(x-1))) / s
print(integ)

#The reason for the resultant integer at the approximation point at 10^-2 is that
#In the derivative and limit definition we are assuming that we are reaching zero
#When we reach the zero assumption is that sigma reaches 0 and the function gives the 0/0 problem
#That is why we are only putting the 1 and the result obtained as 1
#But since we do not yet reach zero our function is not giving the exact solution but gives the close approximate


"""
Q6 - (b) Answer
"""
x = 1
s = 10**-4
#function is x*(x-1)
integ = (((x+s)*((x+s)-1)) - (x*(x-1))) / s
print(integ)

s = 10**-6
#function is x*(x-1)
integ = (((x+s)*((x+s)-1)) - (x*(x-1))) / s
print(integ)

s = 10**-8
#function is x*(x-1)
integ = (((x+s)*((x+s)-1)) - (x*(x-1))) / s
print(integ)

s = 10**-10
#function is x*(x-1)
integ = (((x+s)*((x+s)-1)) - (x*(x-1))) / s
print(integ)

s = 10**-12
#function is x*(x-1)
integ = (((x+s)*((x+s)-1)) - (x*(x-1))) / s
print(integ)

s = 10**-14
#function is x*(x-1)
integ = (((x+s)*((x+s)-1)) - (x*(x-1))) / s
print(integ)

#We understood that limit definition of the derivative function is not a stable approach
#in order to reach the exact value of the derivative
#However, also we observe that the approximation fluctuates nearby the poin1 which is our analytic result of derivative
#Converging to 1 from the upper bound and lower bound indicates that even if it is not stable
#Whenever we are getting to zero our function will get close to 1

"""
Q7 - (a) Answer
"""
import math
h_width = 2/100
start = -1
end = 1
s = 0
while start < end:
    f = math.sqrt(1-(start**2))
    start = start + h_width
    s += h_width * f 
print(s)
#The result compare to the value of the pi/2 is not sustain our expectations
#The result is 1.5691342555492493 which is close to the correct result but not equal

"""
Q7 - (b) Answer
"""

def Run():
    h_width = 2/500000
    start = -1
    end = 1
    s = 0
    while start < end:
        f = math.sqrt(1-(start**2))
        start = start + h_width
        s += h_width * f 
    #print(s)
%timeit Run()

#N:100 => 1.5691342555492493 => 26.3 µs ± 97.3 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
#N:200 => 1.5702085158895212 => 52.1 µs ± 64 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
#N:300 => 1.5704763303905214 => 52.1 µs ± 78.2 µs ± 208 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)


#Increasing the N value will be helpful in order to obtain the exact value of the integral
#In each increase we are shrinking the rectangle area but increasing the amount of the rectangles that cover the area
#Contrary to the previous case, calculating the area with smaller rectangle coverage will result in a better solution which close to the real value
# Increasing the runtime to 1 minute will increase the complexity but will also increase the coverage of the area
