import numpy as np
x = np.random.uniform(0,3,size=(10,6))
print("The orginal matrix is :\n",x)
x[x < .3] = 0
print("The filtered matrix is :\n",x)
