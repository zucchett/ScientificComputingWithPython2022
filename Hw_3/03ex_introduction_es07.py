import math
import timeit

def circle(x): 
    return math.sqrt(1-x*x) 
a=-1
b=1
def integral(circle, N): 
    h= (b-a)/N
    I=0
    for i in range(0,N):
        del_x=h*i+a
        I=h*circle(del_x)
    return I

#A
accurate=integral(circle,100)
integral_result=integral(circle, 100)
print("Accurate is:",accurate ,"Integral with N=100:", (math.pi/2-integral_result)) 


#B

starttime = timeit.default_timer()
b_accurate = integral(circle, 105000000)
endtime = timeit.default_timer()

print("Erorr: ", b_accurate, "N: 105000000", "Result: ", (math.pi/2 - b_accurate))

print("The time difference is :", endtime - starttime)

# When N increases, the result becomes close the right result.
# For this example N= 105000000 takes nearly 1 minute and its result is more accurate than N=100.