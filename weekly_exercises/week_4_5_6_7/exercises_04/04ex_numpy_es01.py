# EXE 1
import numpy as np

m = np.arange(12).reshape((3, 4))
print("matrix = \n", m)
print("\n>> total mean =", m.mean())
print("\n>> Rows ")
row = (m.mean(1)).tolist()
for x in range(len(row)):
    print("mean row", x, "=", row[x])
print("\n>> Columns ")
column = (m.mean(0)).tolist()
for x in range(len(column)):
    print("mean column", x, "=", column[x])
