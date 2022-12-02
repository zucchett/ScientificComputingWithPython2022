"""
2. Color-coded scatter plot

Produce a scatter plot from a dataset with two categories.

Write a function that generates a 2D dataset consisting of 2 categories. Each category should distribute as a 2D gaussian with a given mean and standard deviation. Set different values of the mean and standard deviation between the two samples.
Display the dataset in a scatter plot marking the two categories with different marker colors.
An example is given below:
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import Image

Image('images/two_categories_scatter_plot.png')


def cate(meanList, covList, N):
    data_1 = cate_data(meanList[0], covList[0], N)
    data_2 = cate_data(meanList[1], covList[1], N)
    return cate_df(data_1), cate_df(data_2)


def cate_data(mean, cov, N):
    return np.intrandom.multivariate_normal(mean, cov, N)


def cate_df(data):
    return pd.DataFrame(data, columns=["x", "y"])


mean = ([2, 3], [6, 9])
covariance = ([[-5, 0], [0, 5]], [[-3, 0], [0, 2]])
N = 500

df1, df2 = cate(mean, covariance, N)

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111)
ax.set_title("Scatter Plot", fontsize=20)
ax.scatter(x="x", y="y", data=df1, marker="*", c="red", s=100, alpha=0.7)
ax.scatter(x="x", y="y", data=df2, marker="*", c="black", s=100, alpha=0.7)
plt.show()
