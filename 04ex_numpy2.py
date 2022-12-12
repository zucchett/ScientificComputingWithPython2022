import numpy as np
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

#Using the function outer in numpy:
result_1 = np.outer(u,v)
print(result_1,"\n")

#Using the nested for loop:
V = []
for i in u:
    row = []
    for j in v:
        row.append(i * j)
    V.append(row)
print(V,"\n")

#Using the numpy broadcasting operation:
u_v =u * v.reshape(4,1)
print(u_v.transpose())
