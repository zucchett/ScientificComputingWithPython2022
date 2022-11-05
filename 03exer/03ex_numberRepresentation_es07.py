#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import timeit
import math

def riemann(N):
    integ = 0
    h = 2/N
    for k in range(N):
        x_k = -1+(1/N) + k*h
        y_k = math.sqrt(1-x_k**2)
        integ += h*y_k
    return integ



a= riemann(100)
print("The result of the function for N = 100 is: ",a)
print(format(timeit.timeit(lambda: riemann(2400000), number = 1),".4f"),"seconds")
b = riemann(2400000)
print("The result of the integral for a execution time equal to a second is: ",b)
print(format(timeit.timeit(lambda: riemann(110000000), number = 1),".4f"),"seconds")
c = riemann(110000000)
print("The result of the integral for a execution time equal to a minute is: ",c)
print("The difference between the result for N = 110000000 and the real value is: ",math.pi/2-c)


#a) I find a result with the first two digits equal to the real value
#b)N can be increased up to 2.4 * 10e+6. With an execution time around 1 minute I find an accuracy around 10^-14