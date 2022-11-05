from cmath import sqrt
import math
import timeit

N = 100#number slices
x = -1 #starting value of x (-1<x<1)

integral = math.pi/2 #the expected result

#a
def reimannInt(N,x):
    r_sum =0
    h = 2/N #width of the slices
    for i in range(N):
        r_sum = r_sum + h*sqrt(1-x**2)
        x +=h
    return r_sum
    
print("The true value of the integral: ", integral)
print("The value obtained with Riemann definition: ", reimannInt(N,x))

#The two solutions are very close, and approximated by the first decimals they are the same

#b
time_lim = 1

def computeN(start_N, time_lim, x):
    N = start_N
    time_lim = time_lim
    cond = True
    final_N = -1
    
    while (cond): 
        start_time = timeit.default_timer()
        result = reimannInt(N,x)
        end_time = timeit.default_timer()
        time = end_time - start_time
        
        print("N: ",N)
        print("Time: ", time, " sec")
        
        if (time >= time_lim):
           cond = False
        elif(time< time_lim):
            final_N = N
            N = 2*N
    print("Accuracy: ", math.pi/2-result)
    return final_N
            
N_1 = 10**3
N_2 = 10**6
print("If the computation needs to be run in less than a second N is ",computeN(N_1,1,x))   
print("If the computation needs to be run in less than a minute N is ",computeN(N_2,60,x))   

#Comparing the two accuracies we can notice that they are really close, so there
#is no evident gain