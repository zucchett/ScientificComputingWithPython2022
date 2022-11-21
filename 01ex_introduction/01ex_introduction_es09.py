from math import sqrt
l = [x**2 for x in range(100)]
L = []
for a in range(1,100):
    for b in range(1,100):
        x = a**2 + b**2
        if x in l:
            c = int(sqrt(x))
            if [b,a,c] not in L:
                L.append([a,b,c])
L = tuple(L)
print(L)
