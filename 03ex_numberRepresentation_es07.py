import math
N =100
lim1 = -1

lim2 = 1


h = (lim2 - lim1) / N
I = 0 

for item in range(N):
    x = lim1 + h * item
    y_k = math.sqrt(1-x**2)
    I += h* y_k
print(I)
print(math.pi/2)




































