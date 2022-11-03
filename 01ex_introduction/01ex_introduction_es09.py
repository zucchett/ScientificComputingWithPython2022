import math
l =[]
for x in range(1,100):
    for i in range(1,100):
        z = x**2 + i **2
        z = math.sqrt(z)
        r = z- int(z)
        if r == 0:
            l.append((x, i, z))
print(l)
pythagorean_tripples = [a,b,c for a in range(1,100)]
