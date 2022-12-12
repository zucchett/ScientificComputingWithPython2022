import numpy as np
import matplotlib.pyplot as plt

def gaussian_dist(m,s,N) : 
    x = np.random.normal(m, s, N)
    y = np.random.normal(m, s, N)
    return x,y

N = 300
m1 = 7
s1 = 0.4
x1, y1 = gaussian_dist(m1, s1, N)
plt.scatter(x1,y1)

m1 = 6
s1 = 0.2
x1, y1 = gaussian_dist(m1, s1, N)
plt.scatter(x1,y1)

plt.show()
