import math
vector = [1,2,4]
alist =[]
x = 0
for i in vector:
    x = x + i**2
y = math.sqrt(x)
print(y)
for i in vector:
        z = i/y
        alist.append(z)
print(alist)    
