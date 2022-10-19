#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import math
list = []

n = int(input("Insert the dimension of the vector: " ))
sum = 0

for i in range(0,n):
    element = int(input("x"+str(i+1) + "= "))
    list.append(element)
    sum += list[i]**2

fatt = 1/math.sqrt(sum)

for i in range(len(list)):
    list[i] = list[i]*fatt

print(list)