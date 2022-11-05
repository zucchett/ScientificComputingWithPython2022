#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import math
t = ()
lista = list(t)

n = int(input("Insert the dimension of the vector: " ))
sum = 0

for i in range(0,n):
    element = int(input("x"+str(i+1) + "= "))
    lista.append(element)
    sum += lista[i]**2

fatt = 1/math.sqrt(sum)

for i in range(len(lista)):
    lista[i] = lista[i]*fatt
t = tuple(lista)
print(t)