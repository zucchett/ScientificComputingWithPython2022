# EXE 2
import numpy as np
'''
# arange => crea matrice con primo valore, valore finale, step
print(np.arange(0, 40, 10))

# ripete il vettore x3 righe
a = np.tile(np.arange(0, 40, 10), (3, 1))
print("tile:", '\n', a, '\n')

# 3,2 => ripete il vettore x3 righe e x2 volte nelle colonne
a = np.tile(np.arange(0, 40, 10), (3,2))
print("tile T:", '\n', a, '\n')

# ripete il vettore x3 righe ed effettua il Transpose
a = np.tile(np.arange(0, 40, 10), (3, 1)).T
print("tile:", '\n', a, '\n')
'''

#print("broadcasted sum:", '\n', a + np.arange(3), '\n')



# how to work sum broadcast
'''
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
print(x, y)
b = np.broadcast(x, y)
out = np.empty(b.shape)
out.flat = [u + v for (u, v) in b]
print(out)
'''

a = np.linspace(0,99,100)  # 15 random int between 0 and 21
print("original array:", a, '\n')

# create a mask to filter multiples of 3
mask = [all(x % y != 0 for y in range(2, x)) for x in range(2, len(a))]
print("the mask:", mask, '\n')

filtered_a = a[mask]
# equivalent to a[a % 3 == 0]
print("the filtered array:", filtered_a, '\n')

# verify that fancy indexing creates copies
print("are a and filtered_a the same object?",
      np.may_share_memory(a, filtered_a), '\n')

# Indexing with a mask can be very useful to assign a new value to a sub-array
a[a % 3 == 0] = -1
print("the modified array:", a, '\n')