"""
4. Kernel Density Estimate

Produce a KDE for a given distribution (by hand, not using seaborn):

Fill a numpy array x of length N (with ) with a variable normally distributed, with a given mean and standard deviation
Fill an histogram in pyplot taking proper care of the aesthetic:
use a meaningful number of bins
set a proper y axis label
set proper value of y axis major ticks labels (e.g. you want to display only integer labels)
display the histograms as data points with errors (the error being the poisson uncertainty)
For every element of x, create a gaussian with the mean corresponding to the element value and the standard deviation as a parameter that can be tuned. The standard deviation default value should be:

you can use the scipy function stats.norm() for that.

In a separate plot (to be placed beside the original histogram), plot all the gaussian functions so obtained
Sum (with np.sum()) all the gaussian functions and normalize the result such that the integral matches the integral of the original histogram.
For that you could use the scipy.integrate.trapz() method. Superimpose the normalized sum of all gaussians to the first histogram.
"""
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(scale=10, size=100)
print(arr)

fig, ax = plt.subplots(figsize=(5, 5))
y, bins, patches = plt.hist(arr, bins=25, density=True)

ax.set_title('Kernel Density')
ax.set_xlabel('x')

centers = 0.5 * (bins[:-1] + bins[1:])

fig.tight_layout()
plt.show()


#Superimpose the normalized sum of all gaussians to the first histogram
from scipy.stats import norm

loc = 0
std_dev = 5
size = 50
x = np.random.normal(loc=loc, scale=std_dev, size=size)
mean = x
std_dev = 1.06 * np.std(x) * len(x) ** (-1 / 5)
x_points = np.linspace(np.min(mean) - 3 * std_dev, np.max(mean) + 3 * std_dev, 100)
y_points = np.array([norm.pdf(x_points, mean[i], std_dev) for i in range(len(x))])
for i in y_points: plt.plot(x_points, i)
plt.xlabel('Gaussian Samples')
plt.ylabel('Counts')

plt.show()
