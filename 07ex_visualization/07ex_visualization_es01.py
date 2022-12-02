"""
1. Spotting correlations
Load the remote file:
https://www.dropbox.com/s/aamg1apjhclecka/regression_generated.csv
with Pandas and create scatter plots with all possible combinations of the following features:
features_1
features_2
features_3
Are these features correlated?
"""
from IPython.display import Image
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
filename = 'regression_generated.csv'
data = csv.reader(open(filename, newline=''), delimiter=',')
header = next(data)  # skip first line
dataset = list(data)
x_len = len(dataset[1])
y_len = len(dataset)
print(x_len, y_len)
features1 = list()
features2 = list()
features3 = list()
y = list()
for i in range(1, y_len):
    print(dataset[i][2])
    features1.append(dataset[i][1])
    features2.append(dataset[i][2])
    features3.append(dataset[i][3])
    y.append(i)

plt.scatter(features1, y)
plt.scatter(features2, y)
plt.scatter(features3, y)
plt.show()