import numpy as np
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

result_1 = np.outer(u,v)
print("Result of using numpy outer function is:",result_1,"\n")

#Using the nested for loop:
V = []
for i in u:
    row = []
    for j in v:
        row.append(i * j)
    V.append(row)
print("Result of using nested `for` loop:",V,"\n")

u_v =u * v.reshape(4,1)
print("Result of using broadcasting",u_v.transpose(),"\n")