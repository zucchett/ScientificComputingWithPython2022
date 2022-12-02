#actually, i need more time to underestand this topic, sorry but i miss the deadline, i write this because it is important for me to inform you this lecture is important for me,and i will be solve my problems as soon as possible


import pandas as pd

import numpy as np
import csv
#1)
from random import random, seed
#seed(0)
L = [ int(random()*10) for i in range(10) ]
print("list l:\n ", L, "\n")

with open("./data_int.txt", mode = 'w') as f:
    #f.write(str(L))
    for item in L:
        f.write("%s " % item)

print("loded txt list file:")
!cat ./data_int.txt
print('\n')

#2)
b= np.random.random((5,5))
mat = np.matrix(b)
print("random 5*5 matrix:\n", mat, "\n")
with open('data_float.txt','wb') as f:
    #f.write(str(mat))
    for line in mat:
        np.savetxt(f, line, fmt='%.2f')

print("data_float:")
!cat ./data_float.txt
print('\n')

#3)
f = open('./data_float.txt', 'r')
textContent = f.read()
print("loded txt file: \n", textContent)
f.close()



import zlib
lines = textContent.splitlines()
rawContent = [line.split(' ') for line in lines]
rows = zip(*[rawContent]*1)
with open('data_float.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    for row in rows:
        writer.writerows(row)
print("csv file: ")
!cat ./data_float.csv
print('\n')