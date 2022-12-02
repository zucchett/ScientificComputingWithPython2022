#actually, i need more time to underestand this topic, sorry but i miss the deadline, i write this because it is important for me to inform you this lecture is important for me,and i will be solve my problems as soon as possible


import numpy as np


import matplotlib.pyplot as plt

def gaussian(mean,sta_dev) :
    return np.random.normal(mean,sta_dev,200)

x1 = gaussian(1,0.5)
y1 = gaussian(1,0.5)
plt.scatter(x1,y1)

x2 = gaussian(0,0.4)
y2 = gaussian(0,0.4)
plt.scatter(x2,y2)

plt.show()