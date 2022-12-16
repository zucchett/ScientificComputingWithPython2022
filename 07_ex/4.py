#actually, i need more time to underestand this topic, sorry but i miss the deadline, i write this because it is important for me to inform you this lecture is important for me,and i will be solve my problems as soon as possible


import numpy as np
from scipy import integrate
from scipy.stats import norm
import matplotlib.pyplot as plt
#normally distributed numpy array, x, of len(N) (with N=O(100))
mu, sigma = 10, 2
N=100
x = np.random.normal(mu, sigma, N)
#Fill an histogram
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
Nbins=10
bins=np.arange(x.min(), x.max(), (x.max()-x.min())/Nbins)
freq, bins, patches = ax1.hist(x=x, bins=bins,alpha=1, histtype='bar', rwidth=0.8)
ax1.grid()
ax1.set_xlabel('x')
ax1.set_ylabel('frequencies')
#error part of the question
bincenters = (bins[1:] + bins[:-1])/2
ax1.errorbar(x=bincenters, y=freq, yerr=np.sqrt(freq), fmt='x', c='b', marker='*', markersize=4, capsize=5)
#create a gaussian with the mean corresponding to the element
std_def = 1.06 * x.std() * (x.size ** -0.2)
xrange = np.arange(x.min()-sigma, x.max()+sigma)
gaussians = []
for i, dat in enumerate(x):
    gaussians.append( norm(loc=dat, scale=std_def).pdf(xrange) )
    ax2.plot(xrange, gaussians[i], alpha=0.5)
ax2.set_xlabel('x')
ax2.set_ylabel('f(x)')
ax2.grid()
#Sum (with np.sum()) all the gaussian functions and normalize the result such that the integral matches the integral
#of the original histogram.
area=integrate.trapz(freq, dx=bins[1]-bins[0])
kde=np.array(gaussians).sum(axis=0)
ax1.plot(xrange,kde/sum(kde)*area)
plt.show()