# 7. Integral of a semicircle

# Consider the integral of the semicircle of radius 1:
# 𝐼=∫1−1(⎯⎯√1−𝑥2)d𝑥
 
# which is known to be  𝐼=𝜋2=1.57079632679... .

# Alternatively we can use the Riemann definition of the integral:
# 𝐼=lim𝑁→∞∑𝑘=1𝑁ℎ𝑦𝑘
 
# with  ℎ=2/𝑁  the width of each of the  𝑁  slices the domain is divided into and where  𝑦𝑘  is the value of the function at the  𝑘− th slice.

# (a) Write a program to compute the integral with  𝑁=100 . How does the result compare to the true value?

# (b) How much can  𝑁  be increased if the computation needs to be run in less than a second? What is the gain in running it for 1 minute? Use timeit to measure the time.

# -------------------------------------- Code Begin-------------------------------------

import math,timeit

print('----------------------- Question a ---------------------')
def integral(N):
    h=2/N
    integral=0
    x=[ -1 + i*h for i in range(N) ]
    return sum([h*math.sqrt(1-i**2) for i in x])
print("the value of the semicircle integral for n=100 is", integral(100))
print("the true value is", math.pi/2)
print("the difference between the true value and the calculated value is", math.pi/2 -  integral(100))

# difference between the true value and the calculated value using the Riemann definition is
# is small 0.0016 but it still can  be minimzed by taking a bigger N value
    
print('----------------------- Question b ---------------------')

N = 100

while(True):
    start=timeit.default_timer()
    integral(N)	
    end=timeit.default_timer()
    time= abs(end-start)
    if(time>=1):
        break
    elif(time >0 and time <0.90):
        N*=2
    else:
        N+=1
	
print("the max N to compute the integral in < 1 sec is ", N)
print("the difference between the true value and the calculated value ( 1 min ) is ", math.pi/2 - integral(N*60))
# The difference is 9.920952948050399e-13
# The more N increase the more the calculated value get closer to the True value
# But the more N increase the more the execution time aslo inrease

# -------------------------------------- Code End  -------------------------------------
