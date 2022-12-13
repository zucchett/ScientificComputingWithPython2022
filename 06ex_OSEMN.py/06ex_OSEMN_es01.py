import numpy as np
import csv
import zlib
def List(num1, num2):
  i= []
  while(num1 < num2+1 ):
   i.append(num1)
   num1 += 1
  return i
num1, num2 = -100, 100
a=List(num1, num2)
print(a)
with open('data_int.txt', 'w') as f:
    for item in a:
              f.write("%s " % item)
# cat data_int.txt
   # section b
x = np.random.random((5,5))
matrix = np.matrix(x)
print(matrix)
with open('data_float.txt','wb') as f:
    for line in matrix:
        np.savetxt(f, line, fmt='%.2f')
#cat data_float.txt     

with open('data_float.txt', 'r') as in_file:
    lines = in_file.read().splitlines()
    tab= [line.replace(","," ").split() for line in lines]
    compressed = zip(*[tab]*1)
    with open('data_float.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        for j in compressed:
            writer.writerows(j)