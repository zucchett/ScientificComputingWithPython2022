import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(4, 5, (2, 100))
y = np.random.normal(1, 1.5, (2, 100))

plt.scatter(x = x[0], y = x[1], marker = '*')
plt.scatter(x = y[0], y = y[1], marker = 'o')
plt.show()
