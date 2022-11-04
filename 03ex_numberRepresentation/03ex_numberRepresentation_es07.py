import math as m
import timeit
import time
#Part a:
def Integral(N):
    I=0
    for i in range(N):
        x = -1 + (i*2/N) #The span of (-1,1) is devided to 100 steps
        I+= m.sqrt(1- x**2) * 2/N
    return I

print("Real Area: ", m.pi/2)
print("Calculated Area: ", Integral(100))

#Part b: for 1 Second calculation
startTime = time.time()
difTime=0
n = 100
while difTime< 1:
    n += 100
    Integral(n)
    difTime = time.time()-startTime
    print("dif time : ", difTime)
    
print("Execuation time: ", difTime, "and steps for n is: ", n) 

#Part b: for 5 Second calculation
startTime = time.time()
difTime=0
n = 100
while difTime < 5:
    n += 100
    Integral(n)
    difTime = time.time()-startTime
    print("dif time : ", difTime)
    
print("Execuation time: ", difTime, "and steps for n is: ", n)