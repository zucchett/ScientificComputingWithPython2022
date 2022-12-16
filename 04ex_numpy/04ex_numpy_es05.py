import numpy as np
n1 = np.array(range(1,11))
n2 = np.array(range(1,11))
l = [a *b for a in n1[0:10] for b in n2[0:10]]
l = np.array(l)
l = l.reshape(10,10)
print("This is the original matrix:\n",l)
print("\nThis is the trace of the matrix:\n", np.trace(l))
print("\nThis is Shifted diagonal matrix:\n",(np.roll(l,-1)).diagonal()[0:9])
l = np.fliplr(l)
print("\nThis is Anti-diagonal matrix:\n",l.diagonal())
