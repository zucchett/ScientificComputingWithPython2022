import math

x = (4,1,7,10)
sq = [i**2 for i in x]
norm = math.sqrt(sum(sq))
x_norm = tuple([i/norm for i in x])
print(x_norm)

