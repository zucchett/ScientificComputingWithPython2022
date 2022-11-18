#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import numpy as np

u = np.array([i+1 for i in range(10)])
v = np.array([j+1 for j in range(10)])

tabel = np.outer(u,v)
print(tabel)

#for loop for trace calculation
summa = 0
for i in range(10):
    for j in range(10):
        if i== j:
            summa += tabel[i][j]       
        else:
            pass

print("The trace of the matrix is: ",summa)
#Anti-diagonal matrix elements
m = np.array([tabel[i][-j-1] for i in range(10) for j in range(10) if i==j])
print("The anti-diagonal matrix elements are: ",m)
n = np.array([tabel[i][j+1] for i in range(10) for j in range(9) if i==j])
print("The diagonal matrix elements offset by 1 upwards are:",n)