# 1.Number Representation
def Convert(number, output):
    if output == bin:
        number = bin(number)
    elif output == hex:
        number = hex(number)
    elif output == int or float:
        number = int(number)
    print(number)


Convert(0xa, bin)
Convert(12, hex)
Convert(0b111011, hex)

#2. 32-bit floating point number
binary = 110000101011000000000000
bins = str(binary)
s = bins[0]
e = int(bins[1:9], 2)
f = 0
k = 1
for i in bins[9:33]:
    f = f+int(i)/(2**k)
    k = k+1
float = ((-1)**int(s))*(1+f)*(2**(e-127))
print(float)

#3. Underflow and overflow
import math
Underflow = 1.0
Overflow = 1.0
i = 1
k = 1
#inf = float('inf')
while Underflow != 0.0:
      i = i +1
      Underflow = Underflow/2
print("Underflow exp:",i)
while Overflow != math.inf:
      k = k +1
      Overflow = Overflow*2
print("Overflow exp:",k)

#4. Machine precision
a = 1
b = 1
for i in range(2**100,2**1000):
       i = i +1
       a = a+(1/i)
       b = b+(1/(i-1))
       delta = a-b
       if delta == 0:
          print("Maximum precision value for floating numbers: ",i)
          break

#5. Quadratic solution (Part 1)
import math

def quadraticSolutions(a,b,c):
     delta = math.sqrt(b**2-4*a*c)
     x1 = (-b+delta)/(2*a)
     x2 = (-b-delta)/(2*a)
     return x1,x2
print(quadraticSolutions(0.001,1000,0.001))

#5. Quadratic solution (Part 2)
import math

def quadraticSolutions2(a,b,c):
     delta = math.sqrt(b**2-4*a*c)
     n1 = (-b+delta)
     n2 = (-b-delta)
     x1 = ((-b+delta)*n2)/(2*a*n2)
     x2 = ((-b-delta)*n1)/(2*a*n1)
     return x1,x2
print(quadraticSolutions2(0.001,1000,0.001))

#5. Quadratic solution (part 2)
def quadraticEquation3(a,b,c):
    disc = b**2-4*a*c
    delta = math.sqrt(abs(disc))
    if disc > 0:
       print("Real and different roots: ")
       print((2*c)/(-b-delta))
       print(((2*c))/(-b+delta))
    elif disc == 0:
       print("Real and same roots:")
       print(2*c / (-b))
    else:
       print(-b/(2*a),'+i',delta)
       print(-b/(2*a), '-i', delta)
quadraticEquation3(0.001,1000,0.001)

#6. The derivative
delta = 10**(-2)
x=1
derivateDefinition = (((x+delta)**2-(x+delta)) - (x**2-x))/delta
print("Definition of Derivate: ",derivateDefinition)
realDerivate=2*x - 1
print("Analytical Derivate: ",realDerivate)
print("The two results are different. This is because the analytical derivative is an approximation of the real derivative calculus")
for i in range(2,16,2):
    delta = 10**(-i)
    derivateDefinition = (((x+delta)**2-(x+delta)) - (x**2-x))/delta
    print("Derivate with delta =", delta, "Result=", derivateDefinition)
    print("Difference with analytical value", realDerivate - derivateDefinition)
print("Minimum difference with the analytical value is reach for 10**(-12)")

#7.Integral of a semicircle
import math
import timeit
realvalue = 1.5707963267948986
start = timeit.timeit()
def riemannIntegral(N):
    a = 0
    for k in range(1,N+1):
        a = a + (2/N)*math.sqrt((1-(k/N)**2))
    return a
riemannValue = riemannIntegral(100)
print("Riemann Value: ", riemannValue)
print("Real Value - Riemann Value: ", realvalue-riemannValue)
end = timeit.timeit()
print("Real Value - Riemann Value: ", realvalue-a)
t= end-start
print("Time spent:", t)
N2 = 100/t
print("Number of N if the computation needs to be run in less than a second: ", N2)


