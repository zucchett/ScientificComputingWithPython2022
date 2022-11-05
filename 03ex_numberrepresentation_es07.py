import math
import timeit
starttime = timeit.default_timer()
def func(N):
    lim_1 = -1  
    lim_2 = 1
    h = (lim_2 - lim_1) / N
    I = 0 
    for k in range(N):
        x = lim_1 + h * k
        y_k = math.sqrt(1-x**2)
        I += h* y_k
    print(I)
    print(math.pi/2)

# a) The answers is similar but they are different from second float number.
func(100)

# b) if N = 4600000 the code run in less than a second
starttime1 = timeit.default_timer()
func(4600000)
print("The time is about 1 second : " , timeit.default_timer() - starttime1)

# c) if N = 280000000 the code run in less than a minute and the answers is similar but they are different from 11th float number.
starttime2 = timeit.default_timer()
func(280000000)
print("The time is about 1 minute :" , timeit.default_timer() - starttime2)


























