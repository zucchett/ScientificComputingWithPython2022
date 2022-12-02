import numpy as np

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
print(np.outer(u,v))
a = np.zeros((len(u),len(v)), dtype = int)
for i, u_i in enumerate(u):
    for j, v_j in enumerate(v):
        a[i][j] = u_i * v_j
print(a)
print(u[:,np.newaxis] * v)