import numpy as np
import math
x = np.random.randint(0, 9, (1,100))
print("The real vector is:\n",x)
i = math.sqrt(np.sum(np.square(x)))
x = np.divide(x,i)
print("The normalized vector is:\n",x)
print("The sum is:\n",np.sum(np.square(x)))
