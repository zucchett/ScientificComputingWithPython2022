# Outer product

import numpy as np

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

m1 = np.outer(u,v)
m2 = np.array([[u[i]*v[j] for j in range(4)] for i in range(4)])
m3 = u.reshape([4,1]) * v

print("The 2 starting vectors are:")
print(" u: " + str(u))
print(" v: " + str(v))
print("Outer product calculated with .outer funcion:\n" + str(m1))
print("Outer product calculated with (nested) list comprehension:\n" + str(m2))
print("Outer product calculated with broadcasting:\n" + str(m3))
