#7. Integral of a semicircle
import math as m
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

#Part b: for 1 Second computation
startTime = time.time()
difTime=0
N = 100
ans =0
while(int(difTime) < 1):
    N += 100
    ans=Integral(N)
    difTime = time.time()-startTime
    print("dif time : ", int(difTime))
    
print("Execution time: ", difTime, "sec and steps for n is: ", N, "Calculated Area is: ", ans) # N is 36700

#Part b: for 60 Second computation
startTime = time.time()
difTime=0
N = 100
ans = 0
while(int(difTime) < 60):
    N += 100
    ans = Integral(N)
    difTime = time.time()-startTime
    print("dif time : ", int(difTime))
    
print("Execution time: ", difTime, "sec and steps for n is: ", N, "Calculated Area is: ", ans)  # N is 288300
