#ex 1

print("")
print("Number representation")
print("")

a = 15
b = bin(a)
c = hex(a)
output = "hex"


def ConvertBase(n,output):

    n_isbin = False
    n_ishex = False
    n_isdec = False

    try:
        n = int(n,2)
        n_isbin = True
        n = bin(n)
    except:
        try:
            n = int(n,16)
            n_ishex = True
            n = hex(n)
        except:
            n_isdec = True

    if n_isbin:

        if output == "bin":
            pass
        elif output == "dec":
            n = int(n,2)
        else:
            n = int(n,2)
            n = hex(n)

    elif n_ishex:

        if output == "hex":
            pass
        elif output == "dec":
            n = int(n,16)
        else:
            n = int(n,16)
            n = bin(n)

    else:

        if output == "dec":
            pass
        elif output == "bin":
            n = bin(n)
        else:
            n = hex(n)

    return n


print("the input is: ",b)
print("the output need to be: ",output)
print("the output is: ", ConvertBase(b,output))

#ex 2

print("")
print("32-bit floating point number")
print("")

binnum = "110000101011000000000000"

def bin2float(bin):

    s = binnum[0]
    e = binnum[1:9]
    e_bias = int(e,2)
    e_unbias = e_bias - 127

    j = 1
    i = 9
    f = 0

    while i < len(binnum):
        binnum1 = int(binnum[i])
        f = f+(binnum1*(2**(-j)))
        j = j + 1
        i = i + 1

    decnum = (1+f)*(2**(e_unbias))

    if int(s) == 1:
        decnum = "-"+str(decnum)

    return decnum

print(bin2float(binnum))

#ex 3

print("")
print("Underflow and overflow")
print("")

import sys
print(sys.float_info)
print("")

num_o = 1.0
num_u = 1.0

while num_u > 0:
    num_u = num_u/2
    print(num_u)

print("min = 5e-324")

while num_o < float('inf'):
    num_o = num_o*2
    print(num_o)

print("max = 8.98846567431158e+307")

#ex 4

print("")
print("Machine precision")
print("")

val = 1.0
val_1 = 1.0
lista = []
lista1 = []
i = 0

while True:
    lista.append(val_1)
    lista1.append(val)
    val_1 = val_1+val
    val = val/2
    if val_1 == lista[i]:
        break
    i = i + 1

print(sys.float_info)
print("")
print("the minimum relevant value:",lista1[len(lista1)-2],"which corrisponds to epsilon")
#print(lista1[len(lista1)-4:len(lista1)])
print(lista[len(lista)-4:len(lista)])
print("by adding ",lista1[len(lista1)-2],"to ",lista[len(lista)-3],"we get ",lista[len(lista)-2])

#ex 5

print("")
print("Quadratic solution")
print("")

from math import *

def QuadraticSolution(a,b,c):

    delta = b**2 - 4*a*c
    pos_formula = (-b + sqrt(delta))/(2*a)
    neg_formula = (-b - sqrt(delta))/(2*a)

    return pos_formula,neg_formula

a = 0.001
b = 1000
c = 0.001

print(QuadraticSolution(a,b,c))

def QuadraticSolution1(a,b,c):

    delta = b**2 - 4*a*c
    pos_formula = ((-b + sqrt(delta))*(-b - sqrt(delta)))/((2*a)*(-b - sqrt(delta)))
    neg_formula = ((-b - sqrt(delta))*(-b + sqrt(delta)))/((2*a)*(-b + sqrt(delta)))

    return pos_formula,neg_formula


print(QuadraticSolution1(a,b,c))

#in both cases num and den have 6 decimal unit of distance inbetween them, but in the first case
#four of them are before the decimal separator, in the second all of them are after
#the second result has more decimals than the first

def QuadraticSolution2(a,b,c):

    delta = b**2 - 4*a*c
    deltasqrt = sqrt(abs(delta))

    if delta > 0:
        x1 = (-b + deltasqrt)/(2*a)
        x2 = (-b - deltasqrt)/(2*a)

    elif delta == 0:
        x1 = x2 = -b/(2*a)

    else:
        x1 = str(int((-b + deltasqrt)/(2*a))) + "j"
        x2 = str(int((-b - deltasqrt)/(2*a))) + "j"

    return x1,x2

#ex 6

print("")
print("The derivative")
print("")

x = 1
def Derivate(x,delta):
    inc = x+delta
    dfdx = ((inc*(inc-1)) - (x*(x-1)))/delta
    return dfdx

delta = 0.01
print(Derivate(x,delta))
delta = 0.0001
print(Derivate(x,delta))
delta = 0.000001
print(Derivate(x,delta))
delta = 0.00000001 #is the most accurate
print(Derivate(x,delta))
delta = 0.0000000001
print(Derivate(x,delta))
delta = 0.000000000001
print(Derivate(x,delta))
delta = 0.00000000000001
print(Derivate(x,delta))

#the accuracy decreases when delta becomes smaller than 10^-8
#in fact dig = 15 (dig = maximum number of decimal digits that can be faithfully represented in a float)

#ex 7

print("")
print("Integral of a semicircle")
print("")

N = 100

def Integral(N):
    h = 2/N
    I = 0
    for i in range(1,N):
        x = -1 + i*h
        yk = sqrt(1 - x**2)
        I = I+(yk*h)
    return I

print("result: ",Integral(N)," true result: ", pi/2)

import timeit

beginTime = timeit.default_timer()
mode = Integral(N)
endTime = timeit.default_timer()
Time = endTime - beginTime

print("Time to run with N = 100: ",Time)
possible = N/Time

N = round(possible)
time = 0

while time < 0.98:
    N = N+100000
    beginTime = timeit.default_timer()
    mode = Integral(N)
    endTime = timeit.default_timer()
    time = endTime - beginTime

print("Time to run with N =", N,": ", time)
#N can be increased up to 3237765 and run under a second
print("the result is now: ", mode, " closer to: ", pi/2)

'''
N = N*60
beginTime = timeit.default_timer()
mode1 = Integral(N)
endTime = timeit.default_timer()
time1 = endTime - beginTime

print("Time to run with N = ", N," ", time1)
print("the result is now: ", mode1, " closer to: ", pi/2)
'''

#with N=200010180 the time taken is close to one minute (~59.341450496001926) and
#the result is now:  1.5707963267938005  closer to:  1.5707963267948966
