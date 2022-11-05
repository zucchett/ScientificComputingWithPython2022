#4. Machine precision

v = 1
n = 1
c = 0

for i in range(1000):    
    if (c == v):
        break
    c = v
    v += n/2
    print(v)
    n = n/2    
print(n)