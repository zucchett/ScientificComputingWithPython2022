import numpy as np
import random
import numpy.ma as ma
x=np.random.uniform(0,3,size=(10,6))
print(x)
y=ma.masked_less(x,.3)
print(y)
