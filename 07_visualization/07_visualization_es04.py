from scipy import stats
import scipy
from matplotlib.ticker import AutoMinorLocator

N = 60
m = 5
s = 0.5
no_bins = 15

x = m + s * np.random.randn(N)

fig, (plot1, plot2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 6)) 

bins = plot1.hist(x, bins=no_bins, color='g',edgecolor='white')

plot1.set_yticks(np.arange(0, N, 1)) 
error = np.sqrt(bins[0])
bins_center = (bins[1][:-1] + bins[1][1:])*0.5
plot1.errorbar(bins_center, bins[0], yerr=error, fmt='none', color='r', label="error")

std_def = 1.06*x.std() * x.size**(-1/5)
gaussians=[]
space = np.linspace(np.min(x), np.max(x), N)
for item in x:
    nrm = stats.norm(item, std_def)
    gaussians.append(nrm.pdf(space))
    plot2.plot(space, gaussians[-1])
    

area_sog = scipy.integrate.trapz(np.sum(gaussians, axis=0), space)
area_hist = sum(np.diff(bins[1])*bins[0])
k_norm = area_sog/area_hist
norm_sog = np.sum(gaussians, axis=0)/k_norm

plot1.plot(space, norm_sog, color="b", label="KDE")
plot1.legend()
plot1.set_xlabel('x')
plot1.set_ylabel('frequencies')
plot2.set_xlabel('x')
plot2.set_ylabel('f (x)')
plt.show()