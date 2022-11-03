import math
N =100
lim_1 = -1
lim_2 = 1
h = (lim_2 - lim_1) / N
I = 0 
for l in range(N):
    x = lim_1 + h * l
    y_k = math.sqrt(1-x**2)
    I += h* y_k
print(I)
print(math.pi/2)




































