import math
import timeit
def integ(N):
    a = 0
    for i in range(-int(N/2),int(N/2)):
        x = i*2/N + 1/N
        a = a + 2/N * math.sqrt(1-x*x)
    return a

N1 = 100
result = integ(N1)
dev = result - math.pi/2
print("%.30f" % result, " -----  deviation from true value for N = ",N1,"is :",dev)

N2 = 5500000  # This number resluts in 1 minute execution time. (It maybe different a little)
result = integ(N2)
dev = result - math.pi/2
print("%.30f" % result, " -----  deviation from true value for N = ",N2,"is :",dev)

N3 = 60*N2  # This number resluts in 1 minute execution time.
# result = integ(N3)
# dev = result - math.pi/2
# print("%.30f" % result, " -----  deviation from true value for N = ",N3,"is :",dev)

print("execution time per loop for ( N=",N2,") : (wait a little)")
time = timeit.timeit(lambda: integ(N2), number = 5) / 5
print(time)

# As N gets bigger, deviation is smaller and result has better accuracy, but it takes more time to execute.