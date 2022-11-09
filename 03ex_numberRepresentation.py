print("************Exercise 1***********s***")



def convert_2_bin(to_bin):
    print("Binary Converter:","\n")
    bin_to_bin = bin(to_bin)
    print("Value in Binary:",bin_to_bin)
    print(type(bin_to_bin))
  #  print(int(bin_a, 2)) 
def convert_2_dec(num):
    print("Decimal Converter", "\n")
    bin_num = int(num)
    print("Value in Decimal:",bin_num)
    print(type(bin_num))

def convert_2_hex(to_hex):
    print("Hex Converter", "\n")
    to_hex = hex(to_hex)
    print("Value in Hexadecimal:",to_hex)
    print(type(to_hex))
    
to_bin=0x4f
convert_2_bin(to_bin)
to_bin=79
convert_2_bin(to_bin)

num=0x4f
convert_2_dec(num)
num= 0b1001111
convert_2_dec(num)

to_hex=79
convert_2_hex(to_hex)
to_hex = 0b1001111
convert_2_hex(to_hex)



print("************Exercise 2***************")

# function that converts a 32 bit binary string
# into a single precision floating point in decimal representation



def binary_to_float(M):
    sign = 1
    mantissa = 0
    exponent = 0
    
    if M[0] == '0':
        sign = 1
    elif M[0] == '1':
        sign =- 1
    else:
        print("It is not valid.")
    for i in range(9):
        if i == 0:
            exponent += 0
        elif M[i] == '1':
            exponent += 2**(8-i)

    for j in range(23):
        if M[j+9] == '1':
            mantissa += 2**(-j-1)
    mantissa += 1
    sign = sign*mantissa*2**(exponent-127)
    print(sign)


binary_to_float('010000000001000000000000000000000')



print("************Exercise 3***************")

N = 1500
undflow = 1
ovflow = 1

for i in range(N):
    undflow = undflow / 2
    ovflow  = ovflow  * 2
#   print(i,"\t\t","%1.5e"%undflow,"\t\t","%1.5e"%ovflow)

print(" LOWEST IS  1.11254e-308 ",'\n',"HIGHEST IS  8.98847e+307\n")

### to view the underflow and overlow limit  you can uncomment line 85

print("************Exercise 4***************")

N = 60
eps = 1.0
for i in range (N):
    eps = eps /2
    one_Plus_eps = 1.0 + eps
    print ('eps =' , eps , ', one + eps = ', one_Plus_eps )
    
    
print("the addition starts to have no effect at the 53rd value")

print("************Exercise 5***************")

import math 
"""
## a)
a= float(input("enter number 'a'"))
print(a)
b = float(input("enter number 'b'"))
print(b)
c = float(input("enter number 'c'"))
print(c)
"""
a = 0.001
b = 1000
c = 0.001
d = float((b**2) - (4*a*c)) 
sol1 = (-b - math.sqrt(d))/(2*a)  
sol2 = (-b+math.sqrt(d))/(2*a)  
print('The solutions are {0} and {1}'.format(sol1,sol2)) 

## b) The result was the same
print("**************2nd STEP*******************")

d = float((b**2) - (4*a*c))  
factor = (-b - math.sqrt(d))
sol1 = ((-b - math.sqrt(d)) *factor) /((2*a) * factor)  
sol2 = ((-b+math.sqrt(d))* factor)/((2*a) *factor)

print('The solution are {0} and {1}'.format(sol1,sol2)) 

## c)

def quadratic(d):
    print("*************3rd STEP **************")
    if d > 0:
        num_roots = 2
        x1 = (((-b) + math.sqrt(d))/(2*a))     
        x2 = (((-b) - math.sqrt(d))/(2*a))
        print("There are 2 roots: %f and %f" % (x1, x2))
    elif d == 0:
        num_roots = 1
        x = (-b) / 2*a
        print("There is one root: ", x)
    else:
        num_roots = 0
        print("No roots, discriminant < 0.")
        exit()
        
d = float((b**2) - (4*a*c)) 
quadratic(d)

print("************Exercise 6***************")

from sympy import *
import math
x = Symbol('x')
f = x*(x-1)
f_prime = f.diff(x)
print(f_prime)
f_prime = lambdify(x, f_prime)
print("Result of the function with python derivative imp. : ", f_prime(1))

# a) They are not agreeing perfectly because we are not using a h value small enough to ignore
def f(x):
    return x*(x-1)

def derive(function, value):
    h = 1e-2
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom
    # Returns the slope to the third decimal
    return float("%f" % slope)
print("Result of the function with h 0.01 derivative imp. : ", derive(f, 1))

# b) The results gets more accurete when the h value get closer to 0

def f(x):
    return x*(x-1)

def derive2(function, value,h):
   # h = 1e-4
   #  h = 1e-6 
   # h = 1e-8
   # h = 1e-10
   # h = 1e-12
   # h = 1e-14
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom
    return float("%f" % slope)
h = 1e-2
for i in range(0,6):
    h = h * 1e-2
    print("Result of the function with h ","%.14f" % h ," derivative imp. : ", derive2(f, 1,h))
   

print("************Exercise 7***************")
import timeit
def semicircle_calculator(n):
	if(n==0):
		print("wrong data")
		return
	h=2/n
	integral=0
	x=-1
	for i in range(n):
		integral=integral+(h*math.sqrt(1-x**2)) #computing the value of the function and adding it to the sum
		x=x+h #update x
	return integral

print("the value of the integral for n=100 is", semicircle_calculator(100))



semicircle_calculator(100) ## the result is 1.569, which is very close to the real value
k=100
while(True):
	start_time=timeit.default_timer()
	semicircle_calculator(k)	#computing the execution time
	end_time=timeit.default_timer()
	comp_time=end_time-start_time
	if(comp_time>=1): # i stop the first time when i reach the second
		break
	if(comp_time<0.5):
		k=k*2
	elif(0.5<=comp_time<0.9):	#varying the increasing of k when i get closer to the limit
		k=int(k*1.5)
	elif(comp_time>=0.9):
		k=k+1

print("the max steps to compute the integral in less than one second is ", k-1) #k-1 because i stop when i take 1 second or more

