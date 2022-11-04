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

# a) The second float number is different from the answers, the answers are similar.
func(100)

# b) The code run in less than a second if N = 4600000 
starttime1 = timeit.default_timer()
func(4600000)
print("The time is about 1 second : " , timeit.default_timer() - starttime1)

# c) The code run in less than a minute if N = 280000000, 11th float number is different from the answers but the answers are similar.
starttime2 = timeit.default_timer()
func(280000000)
print("The time is about 1 minute :" , timeit.default_timer() - starttime2)

