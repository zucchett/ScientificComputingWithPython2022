import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import math
import numpy as np

data = pd.read_pickle('./residuals_261.pkl')

data = data.item(0)
dists = data["distances"]
resids = data["residuals"]
dataframe = pd.DataFrame(data={"residuals" : resids, "distances" : dists})

dataframe = dataframe[abs(dataframe["residuals"])< 2]

print("This is the cleaned dataset:\n",dataframe)
sb.jointplot(x = "distances", y = "residuals", data = dataframe, kind = "reg")


nbins = int(math.ceil(math.log2(len(dists))) + 1)
_, bins = np.histogram(dists, bins = nbins)
#print(bins)
x = bins[0:bins.size -1] + np.diff(bins)/2
y = []
err_y = []
for n, _ in enumerate(bins[:-1]):
    value = (dataframe["distances"] >= bins[n]) & (dataframe["distances"] < bins[n+1])
    y.append(dataframe[value]["residuals"].mean())
    err_y.append(dataframe[value]["residuals"].std())
y = np.array(y)
err_y = np.array(err_y)
plt.errorbar(x = x, y = y, yerr = err_y, color = "r")
plt.show()
