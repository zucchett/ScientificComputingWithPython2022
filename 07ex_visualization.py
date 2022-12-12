import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import scipy
import pickle
import bench


# Some utility functions
def bin_centers(bin_edges):
    """
    Convert array of bin edges to array of centers. The size of
    output is: bin_edges - 1
    """
    return (bin_edges[1:] + bin_edges[:-1]) / 2


def bin_num_sturge(data_arr):
    """
    Number of bins for a given size data based on Sturge’s rule.
    It takes into account the size of the data to decide on the
    number of bins.
    """
    return int(np.ceil(np.log2(data_arr.size)) + 1)


def bin_num_freedman(data_arr):
    """
    This rule not only considers the sample size but also considers
    the spread of the sample
    """
    arr = pd.Series(data_arr)
    q1 = arr.quantile(0.25)
    q3 = arr.quantile(0.75)
    iqr = q3 - q1
    bin_width = (2 * iqr) / (len(data_arr) ** (1 / 3))
    return int(np.ceil((arr.max() - arr.min()) / bin_width))


@bench.benchmark("Exercise #1")
def exercise1():
    data = pd.read_csv("./data/regression_generated.csv")

    features = ["features_1", "features_2", "features_3"]
    p = sns.pairplot(data[features])

    # As I observed in the resulting plots, all the features quite similar to
    # each other with a normal distribution with mean equal to zero and standard
    # deviation equal to one
    plt.show()
    print("OK")


@bench.benchmark("Exercise #2")
def exercise2():
    d1 = np.random.normal(0.0, 0.6, size=(2, 200))
    d2 = np.random.normal(2.0, 0.5, size=(2, 200))

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(x=d1[0], y=d1[1], marker="o", c="r")
    ax.scatter(x=d2[0], y=d2[1], marker="o", c="g")
    plt.show()


@bench.benchmark("Exercise #3")
def exercise3():
    # Read the Pickle file
    with open("./data/residuals_261.pkl", "rb") as f:
        p = pickle.loads(f.read())

    # Create pandas dataframe
    data = pd.DataFrame(p.tolist())
    # Prune some unnecessary data
    data = data[np.abs(data["residuals"]) < 2]

    # Create joinplot using seaborn
    g = sns.jointplot(x=data["distances"], y=data["residuals"], data=data, kind="reg")

    # Calculate number of appropriate bins using struge's method
    bin_count = bin_num_sturge(data["distances"])

    # Create the histogram tp obtain values and bin edges
    h, bins = np.histogram(data, bins=bin_count)

    # Create the x variable, it should be the bin centers
    x = bin_centers(bins)

    # Create y and err_y arrays from mean and std of residuals values
    y = []
    err_y = []
    for r in zip(bins[:-1], bins[1:]):
        m = data[data["distances"].between(r[0], r[1])]["residuals"].mean()
        s = data[data["distances"].between(r[0], r[1])]["residuals"].std()
        y.append(m)
        err_y.append(s)
    y = np.array(y)
    err_y = np.array(err_y)

    print(f"x: {x}")
    print(f"y: {y}")
    print(f"err_y: {err_y}")

    # Plot the error bars on top of the seaborn scatter plot from before
    plt.errorbar(x=x, y=y, yerr=err_y, color="r")
    plt.show()


@bench.benchmark("Exercise #4")
def exercise4():
    # Create three plots in a row
    fig, axes = plt.subplots(nrows=1, ncols=3)

    # Form a dataset from normal distribution with a given mean and std values
    N = 100
    data = np.random.normal(5.0, 1.0, size=N)
    bin_count = bin_num_freedman(data)
    y, bins, _ = axes[0].hist(data, bins=bin_count, label="Histogram")

    # Calculate integral of histogram
    area_hist = np.sum(y * np.diff(bins))

    # Show error bars right over the histogram
    err = np.sqrt(y)
    bincenters = bin_centers(bins)
    axes[0].errorbar(x=bincenters, y=y, yerr=err, fmt="none", color="r", label="Errors")

    axes[0].set_title("Original histogram")
    axes[0].set_ylabel("Frequency")
    axes[0].legend()

    axes[1].set_title("Gaussians")
    std = 1.06 * data.std() * (data.size ** (-1 / 5))
    gaussians = []
    x_axis = np.linspace(np.min(data), np.max(data), N)
    for x in data:
        g = scipy.stats.norm.pdf(x_axis, x, scale=std)
        axes[1].plot(x_axis, g)
        gaussians.append(g)

    gaussians_sum = np.sum(gaussians, axis=0)
    area_gaussians_sum = scipy.integrate.trapz(gaussians_sum, x_axis)

    norm_factor = area_gaussians_sum / area_hist
    norm_g = gaussians_sum / norm_factor

    axes[2].set_title("Kernel Density Estimate")
    axes[2].plot(x_axis, norm_g, label="Normalized gaussian")
    axes[2].hist(data, bins=bin_count, label="Histogram")
    axes[2].legend()

    plt.show()


exercise1()
exercise2()
exercise3()
exercise4()
