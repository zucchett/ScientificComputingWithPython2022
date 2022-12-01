#3. Matrix masking

import numpy.random as npr

#creating the matrix
a=npr.uniform(0,3,(10,6))
print(a)

#set all entries <0.3 to zero
mask= (a<0.3)
a[mask]=0
print("The filtered array:\n", a)
