# ESERCIZIO 1
def convertBDH(x, representation):
    if not isinstance(x,int):
            try:
                x=int(x,2)
            except:
                x=int(x,16)
    if representation=='bin':
        return bin(x)
    elif representation=='dec':
        return x
    elif representation=='hex':
        return hex(x)
print('_________ESERCIZIO_1__________')
print(convertBDH('0b1100','hex'))
print(convertBDH('0x1100','bin'))
print(convertBDH(1100,'hex'))


# ESERCIZIO 2
print('\n'+'_________ESERCIZIO_2__________')
bin_str='110000101011000000000000'

while len(bin_str)<32:
    bin_str+='0'

sgn='+'
if bin_str[0]=='1':
    sgn= '-'

exp=int(bin_str[1:9],2)-127

mant=bin_str[9:]

x=1
for i in range(1,len(mant)):
    x=x+ int(mant[i-1],2)/pow(2,i)

x=float(sgn+str(x*pow(2,exp)))

print(x)

# ESERCIZIO 3
print('\n'+'_________ESERCIZIO_3__________')
n=1
run=True

while run==True:
    if float(n*2)==float('inf'):
        run=False
    else:
        n=float(n*2)
print(n)

m=1
run=True

while run==True:
    if float(m/2)==0:
        run=False
    else:
        m=float(m/2)
print(m)


# ESERCIZIO 4
print('\n'+'_________ESERCIZIO_4__________')
a=1
n=0
loop=1
run=True

while run==True:
    n_prev=n
    a=a/2
    n=n_prev+a
    loop+=1
    if n==n_prev:
        break
print('Adding ' + str(a)+ ' to x has no effect')




# ESERCIZIO 5
print('\n'+'_________ESERCIZIO_5__________')
import math
import cmath
def roots(a,b,c):
    if (b**2 - 4*a*c) >= 0:
        x1 = (-b + math.sqrt(b**2-4*a*c)) / (2*a)
        x2 = (-b - math.sqrt(b**2-4*a*c)) / (2*a)
        return [x1,x2]
    else:
        print("No real roots")

a=0.001
b=1000
c=0.001
print('Roots with function 1 :'+str(roots(a,b,c)))

def roots_mod(a,b,c):
    if (b**2 - 4*a*c) >= 0:
        x1 = ((-b + math.sqrt(b**2-4*a*c))*(-b - math.sqrt(b**2-4*a*c))) / (2*a*(-b - math.sqrt(b**2-4*a*c)))
        x2 = ((-b - math.sqrt(b**2-4*a*c))*(-b + math.sqrt(b**2-4*a*c))) / (2*a*(-b + math.sqrt(b**2-4*a*c)))
        return [x1,x2]
    else:
        print("No real roots")
print('Roots with function 2: '+str(roots_mod(a,b,c)))
#The results in case(b) is slightly different from case(a) due to the fact that the number is represented by
#a limited quantity of bits which reduce the accuracy in the operations, so every time we multiply
# or divide for that number the final result changes a little bit.

def roots_comp(a,b,c):
    x1 = (-b + cmath.sqrt(b**2-4*a*c)) / (2*a)
    x2 = (-b - cmath.sqrt(b**2-4*a*c)) / (2*a)
    return [x1,x2]
print('Roots with function 3: '+str(roots_comp(a,b,c)))

# ESERCIZIO 6
print('\n'+'_________ESERCIZIO_6__________')
def funz(x):
    return x*(x-1)
x=1
delta=1e-2
der=(funz(x+delta)-funz(x))/delta
print('result: '+str(der))
print('true value: '+str(2*x-1))
#The results don't agree perfectly because the second function correspond to the true value of the derivative for
#delta tending to zero. In this case delta=0.01 is still too far from zero so the result is quite different.

deltas=[1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]
for i in deltas:
    print('With delta = '+ str(i)+ ' ----> result = ' +str((funz(x+i)-funz(x))/i))

#With delta>=1e-8 the accuracy increases for smaller value of delta. Instead for delta<=1e-10 the accuracy stop
#increasing and in fact decreases because we are dividing a quantity for a value of delta too small. In these
#cases the representation of delta is no more accurate due to the limited amount of bit in the mantissa field.


# ESERCIZIO 7
print('\n'+'_________ESERCIZIO_7__________')
import math
def semcirc(x):
    return math.sqrt(1-x**2)

def riemann(N):
    xh=[x/(N/2) for x in range(-int(N/2),int(N/2)+1)]
    yh=list(map(semcirc,xh))
    I=0
    for i in yh:
        I+=i
    I=2*I/N
    return I

N=100
I=riemann(N)
print('True value = pi/2 = '+ str(math.pi/2))
print('Result with Riemann = '+ str(I))
print('pi/2 - Result with Riemman = '+str(math.pi/2-I))
# timeit riemmann(N)

# I=1.5707963259730864 with N=1600000 and 994 ms ± 29 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
# The gain in running it for 1 minute is an increasing closeness to the real value pi/2

