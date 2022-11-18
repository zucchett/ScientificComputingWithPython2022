#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import numpy as np
import numpy.random as npr

b = npr.uniform(0., 3.,(10,6))
print("The original matrix is: \n",b)
b[b<0.3]= 0.
print("The modified matrix is: \n",b)
