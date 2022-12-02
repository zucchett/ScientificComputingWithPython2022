import numpy as np
import scipy
import math
import matplotlib.pyplot as plt

fig, ax = plt.subplots(nrows = 1, ncols = 3)

x = np.random.normal(0,2.5,100)
nbins = int(math.ceil(math.log2(len(x))) + 1)
y, bins, _ = ax[0].hist(x, bins = nbins, label = "Histogram")
ax[0].set_ylabel("occurrences")

bin_centers = bins[0:bins.size -1] + np.diff(bins)/2

err = np.sqrt(y)

ax[0].errorbar(x = bin_centers, y = y, yerr = err, fmt = "None", color= "r", label = "Poisson uncertainty")
ax[0].set_title("Original histogram")
ax[0].legend()
std = 1.06 * x.std() * (x.size ** (-1/5))
guss = []
x_sliced = np.linspace(np.min(x), np.max(x), x.size)
for e in x:
    g = scipy.stats.norm.pdf(x_sliced, e, scale = std)
    guss.append(g)
    ax[1].plot(x_sliced, g)

ax[1].set_title("Gaussian functions")
sums = np.sum(guss, axis = 0)
integral_guss = scipy.integrate.trapz(sums, x_sliced)
integral_hist = np.sum(y * np.diff(bins))

norm = sums / (integral_guss / integral_hist)



ax[2].plot(x_sliced, norm, label = "Normalized gaussian")
ax[2].hist(x, bins = nbins, label = "Histogram")
ax[2].set_title("Normalized sum of all gaussians")
ax[2].legend()
plt.show()


