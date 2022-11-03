# Cecilia Rossi      mat 2091484
######################### EX 3 NUMBER REPRESENTATION ###########################

####### Exercise 1

def convertNumRepresentation(num, newtype):
    #fornire newtype: dec = decimale, bin = binario, hex = esadecimale
    if isinstance(num,float):
        raise ValueError('You cannot use this function in order to convert floating point numbers')
    else:
        if isinstance(num,str): #è binario o esadecimale
            if num.startswith('0b'):
                oldtype = 'bin'
                try: 
                    num = int(num,2)
                except: 
                    raise ValueError('The input is not correct')
            elif num.startswith('0x'):
                oldtype = 'hex'
                try:
                    num = int(num, 16)
                except:
                    raise Error('The input is not correct')
        else:
            oldtype = 'dec'
        
        if oldtype != newtype:
            if newtype == 'dec':
                return num
            elif newtype == 'bin':
                return bin(num)
            else:
                return hex(num)
        else:
            return num
            

#Test
a = bin(23)
b = 23
c = hex(23)

print('Binario in Intero: ', a, str(b), convertNumRepresentation(a,'dec'))
print('Intero in Binario: ',  str(b), a, convertNumRepresentation(b,'bin'))
print('Binario in Esadecimale: ', a, c, convertNumRepresentation(a,'hex'))
print('Esadecimale in binario:', c, a, convertNumRepresentation(c,'bin'))
print('Intero in esadecimale: ',b, c, convertNumRepresentation(b,'hex'))
print('Esadecimale in Intero: ', c, b, convertNumRepresentation(c, 'dec'))

####### Exercise 2

def singlePrecisionFloat(binstr):
    bias = 127
    
    #primo bit = segno
    if int(binstr[0]) == 0: 
        s = +1
    else:
        s = -1
    
    #bit dall'1 all'8 = esponente
    espon = binstr[1:9] 
    espon = '0b'+str(espon) 
    e = int(espon,2)
    #mantissa da 9 a 32
    mantissa = binstr[9:32]  
    f = 1
    i = 1
    for m in mantissa:
        f += int(m)/(2**i)
        i += 1
    #Ricostruisco il numero in singola precisione
    float_num = (s*f*(2**(e-bias)))
    return float_num

#Test
a = '00000011111000000000000000000000'
b = '11000000101100000000000000000000'
f_num = singlePrecisionFloat(b)
print(f_num)

####### Exercise 3

underflow = 1.0
overflow = 1.0
up_limit = False
down_limit = False

#Calcolo l'overflow
while not up_limit:
    overflow_new = overflow*2
    if overflow_new == float('inf'):
        up_limit = True
    else:
        overflow = overflow_new

print('The overflow for floating point in my computer is: ', overflow)

#Calcolo l'underflow
while not down_limit:
    underflow_new = underflow/2
    if underflow_new == float(0.0):
        down_limit = True
    else:
        underflow = underflow_new

print('The underflow for floating point in my computer is: ', underflow)

#Trasformo in funzioni

def findOverflow():
    overflow = 1.0
    up_limit = False
    while not up_limit:
        overflow_new = overflow*2
        if overflow_new == float('inf'):
            up_limit = True
        else:
            overflow = overflow_new
    return overflow

def findUnderflow():
    underflow = 1.0
    down_limit = False
    while not down_limit:
        underflow_new = underflow/2
        if underflow_new == float(0.0):
            down_limit = True
        else:
            underflow = underflow_new
    return underflow

print(findOverflow())
print(findUnderflow())

####### Exercise 4

a = 4.5
epsilon = 0.001
accuracy = True

while accuracy:
    if a + epsilon == a:
        accuracy = False
    else:
        epsilon = epsilon/10

print('The machine precision is in the order of: ', epsilon)

#Trasformo in una funzione

def machinePrecision():
    a = 4.5
    epsilon = 0.001
    accuracy = True
    
    while accuracy:
        if a + epsilon == a:
            accuracy = False
        else:
            epsilon = epsilon/10
    
    return epsilon

####### Exercise 5

# Esercizio 5
import math

def quadraticSolution_a(a,b,c):
    #ritorna la soluzione di ax^2 + bx + c = 0
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print('There is no solution to the system')
        return
    elif delta == 0:
        x = - b/(2*a)
        return x
    else:
        x1 = (- b - math.sqrt(delta)) / (2*a)
        x2 = (- b + math.sqrt(delta)) / (2*a)
        return x1, x2

a = 0.001
b = 1000
c = 0.001

(x1, x2) = quadraticSolution_a(a,b,c)

def quadraticSolution_b(a,b,c):
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print('There is no solution to the system')
        return
    elif delta == 0:
        x = 2*c/(-b)
        return x
    else:
        x1 =  2*c / (-b + math.sqrt(delta))
        x2 = 2*c / (- b - math.sqrt(delta))
        return x1, x2

(y1, y2) = quadraticSolution_b(a,b,c)

print('Results of the first function: ', '\n', 'x1 = ', x1, '\n', 'x2 = ', x2, '\n')
print('Results of the second function: ', '\n', 'y1 = ', y1, '\n', 'y2 = ', y2, '\n')
print('The difference between the two results (in %) is: \n\n y1 - x1 = ', abs((y1-x1)/y1)*100, '% \n')
print('y2 - x2 = ', abs((y2-x2)/y2)*100, '% \n')

#ENG
#Since the representation of floating point numbers tends to overcome the correct value, when we compute 'b^2 - 4*a*c', since
# b is an integer and a*c will be a larger value than expected, we will obtain a slightly smaller value than expected. 
#Using the function quadraticSolution_a, we find this negative variation in the numerator and this implies obtaining 
# smaller values of the solutions. 
#Instead, using the function quadraticSolution_b, the negative variation is found in the denominator, so it implies higher (and more accurate)
#values of the solutions. 

#ITA
#Poichè la rappresentazione di numeri in virgola mobile, a causa del numero elevato di bit utilizzati, tente a restituire 
#dei valori più elevati di quelli forniti in input, o che ci aspetteremmo in caso di moltiplicazione, quando eseguiamo l'operazione
# 'b^2 - 4*a*c', in cui b è un intero ed a*c fornirà un valore più elevato di quello atteso, l'operazione fornirà un risultato
#inferiore alle previsioni. 
#Usando la funzione quadraticSolution_a, essendo tale variazione negative situata al numeratore, implicherà dei valori 
#delle soluzioni più bassi di ciò che ci aspetteremmo. 
#Invece, usando la funzione quadraticSolution_b, in cui l'operazione è al denominatore, otterremo delle soluzioni dai valori più elevati. 

def quadraticSolution(a,b,c):
    #ritorna la soluzione di ax^2 + bx + c = 0
    a_per_c = float('%.10f' % (a*c))
    delta = float('%.10f' % ((b**2) - (4*a_per_c)))
    if delta < 0:
        print('There is no solution to the system')
        return
    elif delta == 0:
        x = - b/(2*float('%.10f' % a))
        y = 2*float('%.10f' % c)/(-b)
        x1 = x
        x2 = x
        y1 = y
        y2 = y
        return x1, y1, x2, y2
    else:
        x1 = float('%.10f' % (- b - float('%.10f' % math.sqrt(delta)))) / (2*a)
        y1 = 2*c / float('%.10f' % (- b + float('%.10f' % math.sqrt(delta))))
        x2 = float('%.10f' % (- b + float('%.10f' % math.sqrt(delta)))) / (2*a)
        y2 = 2*c / float('%.10f' % (- b - float('%.10f' % math.sqrt(delta))))
        return x1, y1, x2, y2

(z1, z2, z3, z4) = quadraticSolution(a,b,c)
print('Results using the final function: ', '\n', 'x1 = ', z1, '\n', 'y1 = ', z2, '\n', 'x2 = ', z3, '\n', 'y2 = ', z4)

####### Exercise 6

import matplotlib.pyplot as plt

def f(x):
    return x*(x-1)

def derivate_f(x,sigma):
    return (f(x+sigma)-f(x))/sigma

sigma = 0.01
x = 1
print('Code Result:       ', derivate_f(x,sigma))
result = sigma + 1;
print('Analytical Result: ', result, '\n')

diff = [(result - derivate_f(x,sigma))/result * 100]

for sigma in [10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14]:
    print('Code Result for sigma = ', sigma, ': ', derivate_f(x,sigma))
    print('Correct Analyticsl Result:       ', sigma + 1, '\n')
    diff.append((sigma + 1 - derivate_f(x,sigma))/(sigma + 1) * 100)

plt.plot([2,4,6,8,10,12,14], diff)
plt.xlabel('sigma = 10*(-x)')
plt.ylabel('Result - Derivate_f(1,sigma)')
plt.title('Accuracy scale with respect to sigma')
plt.show

####### Exercise 7

import math
import timeit

#a) 

def semicerchioUnitario(x):
    return math.sqrt(2*x - x*x)

def semicircleIntegral(N):
    I = 0
    for k in range(N):
        I += (2/N)*semicerchioUnitario(2*k/N)
    return I 

N = 100
loops = 100
print('The integral of the semicircle of radius 1 is: ', semicircleIntegral(N))
print('Correct Analytical Result: ', math.pi/2)
print('Difference between the correct result and the code result: ', abs(math.pi/2 - semicircleIntegral(N))/math.pi/2 * 100, '%')

#b)

t = timeit.timeit('semicircleIntegral(N)', globals = globals(), number = loops)
tempo = t/loops
print('The computation runs for ', str(tempo), ' seconds')

while tempo < 1:
    N_new = N * 10
    t_new = timeit.timeit('semicircleIntegral(N_new)', globals = globals(), number = 1)
    tempo = t_new/1
    if not tempo < 1:
        break
    else:
        N = N_new
        t = t_new

print('With N = ', str(N), 'the computation runs for: ', str(t),' seconds')

tempo1 = timeit.timeit('semicircleIntegral(1500000)', globals = globals(), number = 1)
tempo2 = timeit.timeit('semicircleIntegral(N*2 + 50000)', globals = globals(), number = 1)
tempo3 = timeit.timeit('semicircleIntegral(N*2 + 100000)', globals = globals(), number = 1)
print(tempo1)
print(tempo2)
print(tempo3)

#If the computation needs to be run in less than a second, we can increase N till 1000000. Proceding by trial and error, 
# we can discover that we can increase N also till 2050000.

#If we want the code to run for 1 minute, surely N needs to be much higher. Anyway, we wouldn't get a great gain from this, 
#since, also using a much lower value of N, we can obtain a quite accurate result with a more reasonable computational time 
