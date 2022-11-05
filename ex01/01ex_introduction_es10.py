import math
normal_vector = []
four_dimentional = [5,9,1,2]
x = 0
for i in four_dimentional:
    x = x + i*i
    total =math.sqrt(x)
print(total)
for j in four_dimentional:
    normal_vector.append(j/total)
print(normal_vector,sum(normal_vector))




