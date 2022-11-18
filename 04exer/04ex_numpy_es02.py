#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import numpy as np
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
b = np.outer(u,v)
print("The matrix obtained with the outer function is: \n",b)
ut = u.reshape(4,1)

l = np.array([[u[j]*v[i] for i in range(4)] for j in range(4)])
print("The matrix obtained with the list comprehension is: \n",l)
##########broadcasting
g = u.reshape(4,1)*v
print("The matrix obtained with the broadcasting is: \n",g)
if b.any()==l.any()==g.any():
    print("The three methods are equivalent")
else:
    print("Something is wrong!!!")
