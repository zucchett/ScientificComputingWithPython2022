import math
from scipy.integrate import quad

f = lambda x: math.sqrt(1 - x**2)


def Riemann(n):
    
    h=2/n
    y=-1
    I=0
    for k in range(n):
        I+=h*f(y)
        y+=h
    return I


N=100
res, err = quad(f, -1, 1)


print("The integral result is {:f} (+-{:g})".format(res, err))
print("the Riemann result is : " ,Riemann(N) )


N=10**7
for k in range(10**3,N,10**3):
  print("the Riemann result is : " ,Riemann(N) )