# Matrices

import numpy as np

m = np.array([[(i+1)*(j+1) for i in range(10)] for j in range(10)])

#mdiag = np.trace(m)
inc = np.arange(0, 10, 1)
dec = inc[::-1]

mdiag = m[inc, inc]
tr = np.sum(mdiag)

manti = m[dec, inc]

shiftr = np.arange(0, 9, 1)
shiftc = np.arange(1, 10, 1)
mshift = m[shiftr, shiftc]
print("Original matrix is\n" + str(m) + "\n")
print("Diagonal elements are\n" + str(mdiag) + "\nSum is " + str(tr) + "\n")
print("Antidiagonal elements are\n" + str(manti) + "\n")
print("Offset diagonal elements are\n" + str(mshift) + "\n")
