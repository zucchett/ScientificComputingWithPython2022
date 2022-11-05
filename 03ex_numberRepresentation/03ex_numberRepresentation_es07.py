# 7. Integral of a semicircle

# Consider the integral of the semicircle of radius 1

import math
import timeit


def Riemann(n):
    I = 0
    for h in range(1, n+1):
        I = I + ((2/n)*math.sqrt(1-((1/n*h)**2)))
    return I

N = 100
# start_t = timeit.default_timer()
Int_R = Riemann(N)
# end_t = timeit.default_timer()

print("The integral computed with the Riemann definition is " + str(Int_R))

true_v = math.pi/2

print("The true value of the integral is " + str(true_v))

print("The difference between the two is " + str(-Int_R+true_v))

# how much can  be increased if the computation needs
# to be run in less than a second? What is the gain 
# running it for 1 minute? Use timeit to measure the time.

l = 2
i = 0
times = []

while("True"):
    start_t = timeit.default_timer()
    output = Riemann(l)	#computing the execution time
    end_t = timeit.default_timer()
    ex_time = (end_t-start_t)
    times.append(ex_time)
    print("With N = " + str(l) + " slices the execution time is " + str(ex_time))
    if (ex_time >= 0.95 and ex_time < 1) :
        break
    elif (ex_time >= 0.5 and ex_time < 0.85):
        l = l + 8192
    elif (ex_time >= 0.85 and ex_time < 0.95):
    	l = l + 2048
    elif (ex_time < 0.5):
        l = l*2
    else: # ex_time >= 1
    	l = l - 512
    i = i + 1
    
print('\n')

print("Dividing the domain into N = " + str(l) + " slices, the computation of the Riemann integral takes " + str(times[i]) + " s.") 

print('\n')

print("The computation will take some time (we have to wait up to 60 seconds)")

print('\n')

t = 0
K = 60

while(t < 50 or t > 60):

	c = int(K / ex_time)
	M = l * c
	start_t2 = timeit.default_timer()
	output2 = Riemann(M)
	end_t2 = timeit.default_timer()
	ex_time2 = end_t2 - start_t2
	t = ex_time2
	
	if ( t < 50):
		K = K + 10
	elif (t > 60):
		K = K - 10
	
	print("Dividing the domain into N = " + str(M) + " slices, the computation of the Riemann integral takes " + str(ex_time2) + " s.")

	print("Therefore the gain between the two execution times is " + str(ex_time2/ex_time))

# exercise done

