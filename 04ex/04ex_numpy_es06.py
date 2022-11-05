# Broadcasting

import numpy as np

a = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
b = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])

m = np.array([[abs(a[i]-b[j]) for j in range(10)] for i in range(10)])
n = m*1.609344

print("Distances in miles:")
print(str(m) + "\n")
print("Distances in kilometers:")
print(str(n) + "\n")
