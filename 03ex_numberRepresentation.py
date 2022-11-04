print("\nex. 1")

# type the number in the following format
# 0b: binary, 0x: hexadecimal, 0d: decimal.

number = input("Enter a number: ")
typeout = input("Enter the type (bin/dec/hex): ")

number.lower()


def conv (number, typeout):
    if number[1] == "b":
        number=number[2:]
        print(number)
        if typeout == "bin":
            return number
        if typeout == "dec":
            return int(number, 2)
        if typeout == "hex":
            return hex(int(number, 2))                    
    elif number[1] == "x":
        number=number[2:]
        print(number)
        if typeout == "bin":
            return bin(int(number,16))
        if typeout == "dec":
            return int(number,16)
        if typeout == "hex":
            return number
    elif number[1] == "d":
        number=number[2:]
        print(number)
        if typeout == "bin":
            return bin(int(number))
        if typeout == "dec":
            return int(number)
        if typeout == "hex":
            return hex(int(number))
    else:
        return
            
       
ans = conv (number, typeout)
print("The coverted number is: ",ans) 
    
    
    


print("\nex. 2")

# 1 --> sign
# 8 --> esponente
# 23 --> mantissa 

number = input("Enter a 32 bit binary number: ")
number = "110000101011000000000000"

esponent = int(number[1:9], 2) - (127)

mantissa = number [9:]
mantissa = mantissa [::-1]

temp=1
for i in range(len(mantissa)):
    # mantissa is spannometrically correct 
    # so the xfloat is uncorrect
    temp += int(mantissa[i], 2) / (2**i)
    
xfloat = temp * (2**esponent) * ((-1)**int(number[0], 2))
  
print(xfloat)




print("\nex. 3")

number = 1.0

# the minimum representable number is 5e-324
while number > 0:
    number /= 2
    print(number)
    
# the maximum representable number is 8.98846567431158e+307
# overflow
'''
while number < float("inf"):
    number *= 2
    print(number)
'''





print("\nex. 4")

number = 1.0
newnumber = 0.0
i=0

# the  machine precision is -2.220446049250313e-16
while number-newnumber != 0:
    newnumber = number + 1*(2**-i)
    i += 1
    print(number-newnumber)





print("\nex. 5")

from math import sqrt



#point a

def f(a, b, c):
    x1 = (-b+sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b-sqrt((b**2)-(4*a*c)))/(2*a)
    results = [x1, x2]
    return results



# point b
# we can notice a slight decrease in the second root -999999.9999990001
def f1(a, b, c):
    d = sqrt((b**2)-(4*a*c))
    x1 = ((-b+d)*(-b-d))/((2*a)*(-b-d))
    x2 = ((-b-d)*(-b+d))/((2*a)*(-b+d))
    results = [x1, x2]
    return results



#point c
'''
if a == 0:
    f(0,b,c)
elif b==0:
    f(a,0,c)
elif c==0:
    f(a,b,0)
elif a == 0 and b == 0:
    f(0,0,c)
elif a == 0 and c == 0:
    f(0,b,0)
elif b == 0 and c == 0:
    f(a,0,0)
else:
    print("In this case have non sense find the roots because the equation 0=0")
'''

a = 0.001
b = 1000
c = 0.001

f(a,b,c)
print(f(a,b,c))
f1(a,b,c)
print(f1(a,b,c))





print("\nex. 6")

x = 1
def f(x,delta):
    var = x+delta
    return (var*(var-1) - x*(x-1))/delta
    
delta = 0.01
print(f(x, delta))
delta = 0.0001
print(f(x, delta))
delta = 0.000001
print(f(x, delta))
delta = 0.00000001
print(f(x, delta))
delta = 0.0000000001
print(f(x, delta))
delta = 0.000000000001
print(f(x, delta))
delta = 0.00000000000001
print(f(x, delta))

'''
We can notice that have a delta smaller and smaller is 
convenient until 10**(-8), after we can notice some approximation 
errors due to computer representation of numbers.
The important conseguence is that we have a loss of accuracy 
in the final result.
'''





print("\nex. 7")

from math import sqrt

# point a

N = 100

def f(N):
    h = 2/N
    integral = 0
    for i in range(N):
        xk = -1 + h*i
        yk = sqrt(1 - xk**2)
        integral += yk*h
    return integral
    
print(f(N))

# With N = 100 we obtain 1.5691342555492505 estimation 
# of pi/2 with a precision of 10^(-1)



# point b
 
import timeit

N = 4000000
time = 0
lasttime = 0.4

while (lasttime - time) < 1:
    time = timeit.default_timer()
    f(N)
    lasttime = timeit.default_timer()
    print(lasttime-time)
    N += 100000
    
print(N)    #6000000      
print(f(N)) #1.570796326681797 get an estimation of pi/2 with a precision of 10^(-9)


    
    



