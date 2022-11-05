import math
import random

n=int(input("Inserire la lunghezza del vettore: "))
x=[]
i=0
sum=0
while i<n:
	add=random.randint(0,20)	#genero un numero random e lo aggiungo alla lista
	x.append(add)
	i=i+1
	sum=sum+add			#variabile che contiene la somma di tutti gli elementi della lista
print(x)
print("Normalizzazione del vettore:")
y=[]
i=0
sumnorm=0
while i<n:
	norm=x[i]/sum
	y.append(norm)		#utilizzo la proporzione x[i]:sum=norm:1
	sumnorm=sumnorm+norm
	i=i+1
print(y)
print("La somma degli elementi del vettore è:",sumnorm)
