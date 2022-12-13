import numpy as np
import math
import numpy.ma as ma
import matplotlib.pyplot as plt
pi=np.pi
print(pi)
x=np.linspace(0, 2*pi, num=100)
print(x)
# section a
y=x[::10]
print(y)
#section b
print(y[::-1]) #reverse all numbers instead -10 of -1
# section c
diff=np.abs(np.sin(x)-np.cos(x))<0.1
print(x[diff])
plt.scatter(x[diff],np.sin(x[diff]))
plt.plot(x,np.sin(x),x,np.cos(x))
plt.show()

