import numpy as np
n1 = np.array([1,2,3,4,5,6,7,8,9,10])
n2 = np.array([1,2,3,4,5,6,7,8,9,10])
l = [a *b for a in n1[0:10] for b in n2[0:10]]
l = np.array(l)
l = l.reshape(10,10)
print("This is the original matrix:\n",l)
print("This is Shifted diagonal matrix:\n",(np.roll(l,-1)).diagonal()[0:9])
l = np.fliplr(l)
print("This is Anti-diagonal matrix:\n",l.diagonal())
