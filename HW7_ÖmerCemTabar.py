"""
Author : Ömer Cem Tabar
Exercise Document 07 Solution File

This file only includes the codes that is required to solve the questions
You can also check the outputs from the notebook

"""

"""
1\. **Spotting correlations**

Load the remote file:

```bash
https://www.dropbox.com/s/aamg1apjhclecka/regression_generated.csv
```

with Pandas and create scatter plots with all possible combinations of the following features:
    
  + features_1
  + features_2
  + features_3
  
Are these features correlated?
"""
#!wget https://www.dropbox.com/s/aamg1apjhclecka/regression_generated.csv -P data/
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#2000 ROWS & 21 COLUMNS
fileName = 'data/regression_generated.csv'
df = pd.read_csv(fileName)
data_pairs = []
column_names = ['features_1','features_2','features_3']

fig, (ax1, ax2,ax3) = plt.subplots(nrows=1, ncols=3, figsize=(20,6))
ax1.scatter(x=df[column_names[0]], y=df[column_names[1]], marker='x', c='r')
ax1.set_title('features_1 versus features_2')
ax1.set_xlabel('features_1')
ax1.set_ylabel('features_2')

ax2.scatter(x=df[column_names[0]], y=df[column_names[2]], marker='x', c='g')
ax2.set_title('features_1 versus features_3')
ax2.set_xlabel('features_1')
ax2.set_ylabel('features_3')

ax3.scatter(x=df[column_names[1]], y=df[column_names[2]], marker='x', c='b')
ax3.set_title('features_2 versus features_3')
ax3.set_xlabel('features_2')
ax3.set_ylabel('features_3')

corr1 = np.corrcoef(df[column_names[0]], df[column_names[1]])[0,1]
corr2 = np.corrcoef(df[column_names[0]], df[column_names[2]])[0,1]
corr3 = np.corrcoef(df[column_names[1]], df[column_names[2]])[0,1]

print("No correlation between feature_1 and feature_2 since we obtain a small correlation coefficient as: ", corr1)
print("No correlation between feature_1 and feature_3 since we obtain a small correlation coefficient as: ", corr2)
print("No correlation between feature_1 and feature_2 since we obtain a small correlation coefficient as: ", corr3)

#Hence features are not correlated since the linear relationship between all pairs of features are nearly zero
"""
2\. **Color-coded scatter plot**

Produce a scatter plot from a dataset with two categories.

* Write a function that generates a 2D dataset consisting of 2 categories. Each category should distribute as a 2D gaussian with a given mean and standard deviation. Set different values of the mean and standard deviation between the two samples.
* Display the dataset in a scatter plot marking the two categories with different marker colors.

An example is given below:
from IPython.display import Image
Image('images/two_categories_scatter_plot.png')
"""
from numpy import random
import seaborn as sns
import numpy as np
def D2GaussianDataset():
    dataset = []
    firstCategory = []
    secondCategory = []
    firstMeanxs = 1
    firstMeanxy = 1
    secondMeanxs = 0
    secondMeanxy = 0
    firstSTDxs = 0.5
    firstSTDxy = 0.5
    secondSTDxs = 0.4
    secondSTDxy = 0.4
    firstCategoryxs = np.random.normal(firstMeanxs,firstSTDxs,150)
    firstCategoryxy = np.random.normal(firstMeanxy,firstSTDxy,150)
    secondCategoryxs = np.random.normal(secondMeanxs,secondSTDxs,150)
    secondCategoryxy = np.random.normal(secondMeanxy,secondSTDxy,150)
    for i in range(0,len(firstCategoryxs)):
        tp = (firstCategoryxs[i],firstCategoryxy[i])
        firstCategory.append(tp)
    for i in range(0,len(secondCategoryxs)):
        tp = (secondCategoryxs[i],secondCategoryxy[i])
        secondCategory.append(tp)
    
    for i in range(0,len(firstCategory)):
        row = []
        row.append(firstCategory[i][0])
        row.append(firstCategory[i][1])
        row.append(secondCategory[i][0])
        row.append(secondCategory[i][1])
        dataset.append(row)
    dataset = np.array(dataset)
    return dataset
    
dataset = D2GaussianDataset()
fcx = [dataset[i][0] for i in range(0,len(dataset))]
fcy = [dataset[i][1] for i in range(0,len(dataset))]
scx = [dataset[i][2] for i in range(0,len(dataset))]
scy = [dataset[i][3] for i in range(0,len(dataset))]

plt.scatter(fcx,fcy,color = 'yellow')
plt.scatter(scx,scy,color = 'purple')

"""
3\. **Profile plot**

Produce a profile plot from a scatter plot.
* Download the following pickle file:
```bash
wget https://www.dropbox.com/s/3uqleyc3wyz52tr/residuals_261.pkl -P data/
```
* Inspect the dataset, you'll find two variables (features)
* Convert the content to a Pandas Dataframe
* Clean the sample by selecting the entries (rows) with the absolute values of the variable "residual" smaller than 2
* Plot a Seaborn `jointplot` of "residuals" versus "distances", and use seaborn to display a linear regression. 

Comment on the correlation between these variables.

* Create manually (without using seaborn) the profile histogram for the "distance" variable; choose an appropriate binning.
* Obtain 3 numpy arrays:
  * `x`, the array of bin centers of the profile histogram of the "distance" variable
  * `y`, the mean values of the "residuals", estimated in slices (bins) of "distance"
  * `err_y`, the standard deviation of the of the "residuals", estimated in slices (bins) of "distance"
* Plot the profile plot on top of the scatter plot
"""
#!wget https://www.dropbox.com/s/3uqleyc3wyz52tr/residuals_261.pkl -P data/

#Reading the pickle file
import pickle
filename = 'data/residuals_261.pkl'
infile = open(filename, 'rb')
dataset = pickle.load(infile)
infile.close()

#Reading the dataset into dictionary type list
lst  = dataset.tolist()

#Checking the keys and values that contained in the dataset
#print(lst.items)
#print(lst.keys)
#print(lst.values)

#Creation of empty DataFrame and filling with the desired values with respect to their corresponding columns
RedDisDF = pd.DataFrame()
RedDisDF['residuals'] = lst['residuals']
RedDisDF['distances'] = lst['distances']

#Chekcing the information properly with DataFrame properties after the convertion
print(RedDisDF)
print(RedDisDF.info())

#Clean the sample by selecting the entries (rows) with the absolute values of the variable "residual" smaller than 2
RedDisDF.drop( RedDisDF[abs(RedDisDF['residuals']) < 2 ].index , inplace=True)

#Make sure that all the values are sieved (approached with the mask ideology)
RedDisDF=RedDisDF[abs(RedDisDF['residuals'])>2]

#Plotting the jointplot (scatter plot with profile histogram)
sns.jointplot(x="residuals", y="distances", data=RedDisDF, kind="reg") # perform a regression on the data

#Chekcing the correlation between the categories/features
corr = np.corrcoef(RedDisDF['distances'], RedDisDF['residuals'])[0,1]
print("No correlation between distances and residuals since we obtain a small correlation coefficient as: ", corr)
#Hence there is no correlation between distances and residuals

######### CREATE MANUALLY THE PROFILE HISTOGRAM #############
#Creating an empty figure in order to put the grams onto
fig = plt.figure(figsize=(10, 6))

#Adding main axes for the figure
axes = fig.add_axes([0.1, 0.1, 0.65, 0.65])

#Adding axes for the Profile Histogram of distance feature
#Denote that it will share the axes with the created figure
axesProfileHistogram = fig.add_axes([0.1, 0.8, 0.65, 0.2], sharex=axes)
axesProfileHistogram.set_title('Profile Histogram of the Distance Feature')

#Plotting the scatter plot on the figure that we have created
#Use the axes restriction that we have described for the figure(fig)
axes.scatter(RedDisDF['distances'],RedDisDF['residuals'])

#Plotting the profile histogram on the scatter plot that we have been created
#Number of bins have been setted to 11 since we have seen the figure with 11 bins
#as an output of snsplot
h,bins,_ = axesProfileHistogram.hist(RedDisDF['distances'],bins = 11)


#The array of bin centers calculation
x = 0.5*(bins[1:]+bins[:-1])

#For the mean values of residuals we have created an zeros array with bin length
#It will be filled below
y = np.zeros(len(bins))

#For the standar deviation values of residuals we have created an zeros array with bin length
#It will be filled below
err_y = np.zeros(len(bins))

#Filling up the y and err_y arrays properly
for i in range(0,len(x)-1):
    mask = (RedDisDF['distances']>x[i]) & (RedDisDF['distances']<x[i+1])
    y[i] = np.mean(RedDisDF[mask].residuals)
    err_y[i] = np.std(RedDisDF[mask].residuals)
    
#Showing the plot
plt.show()

#Printing out the obtained arrays
print("the array of bin centers of the profile histogram of the 'distance' variable(x):\n\n",x,"\n")
print("the mean values of the 'residuals', estimated in slices (bins) of 'distances'(y):\n\n",y,"\n")
print("the standard deviation of the of the 'residuals', estimated in slices (bins) of 'distance'(err_y):\n\n", err_y,"\n")

"""
4\. **Kernel Density Estimate**

Produce a KDE for a given distribution (by hand, not using seaborn):

* Fill a numpy array `x` of length N (with $N=\mathcal{O}(100)$) with a variable normally distributed, with a given mean and standard deviation
* Fill an histogram in pyplot taking proper care of the aesthetic:
   * use a meaningful number of bins
   * set a proper y axis label
   * set proper value of y axis major ticks labels (e.g. you want to display only integer labels)
   * display the histograms as data points with errors (the error being the poisson uncertainty)
* For every element of `x`, create a gaussian with the mean corresponding to the element value and the standard deviation as a parameter that can be tuned. The standard deviation default value should be:
$$ 1.06 * x.std() * x.size ^{-\frac{1}{5}} $$
you can use the scipy function `stats.norm()` for that.
* In a separate plot (to be placed beside the original histogram), plot all the gaussian functions so obtained
* Sum (with `np.sum()`) all the gaussian functions and normalize the result such that the integral matches the integral of the original histogram. For that you could use the `scipy.integrate.trapz()` method. Superimpose the normalized sum of all gaussians to the first histogram.


"""

import numpy as np
from scipy import integrate
from scipy.stats import norm
import matplotlib.pyplot as plt

#Fill a numpy array 'x' of length N=0(100) with a variable normally distributed
#with a given mean and standard deviation
mean = 1
std = 2
N=100
x = np.random.normal(mean, std, N)

#Create the figure that includes subplots in ax1 and ax2
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
numberOfBins=10
#Use a meaningful number of bins
minimum = x.min()
maximum = x.max()
step = (x.max()-x.min())/numberOfBins
bins=np.arange(minimum, maximum , step)

#Plotting the error histogram
dist, bins, patches = ax1.hist(x=x, bins=bins,alpha=1, histtype='bar', rwidth=0.8)
#Configuring the grid lines
ax1.grid()
#Setting the x label
ax1.set_xlabel('x')
#Setting meaningul y axis label
ax1.set_ylabel('Density')

#The array of bin centers calculation
binss = (bins[1:] + bins[:-1])/2

#Plotting an error bar
ax1.errorbar(x=binss, y=dist, yerr=np.sqrt(dist), c='purple', marker='x', markersize=3, capsize=2)
#For every element of x, creating a gaussian with
# ====> Mean corresponding to that element
# ====> A standard deviation that is calculated as default
standarDeviationDeifinition = 1.06 * x.std() * (x.size ** -0.2)

#Setting a range for gaussianNormalArray
rangeForgaussianNormalArray = np.arange(x.min()-std, x.max()+std)

#Ditrubutions for every element in x
gaussianDistributions = []
for index, meanElement in enumerate(x):
    gaussianDistributions.append( norm(loc=meanElement, scale=standarDeviationDeifinition).pdf(rangeForgaussianNormalArray) )
    ax2.plot(rangeForgaussianNormalArray, gaussianDistributions[index], alpha=0.5)
    
#Setting the x label
ax2.set_xlabel('x')
#Setting the y label
ax2.set_ylabel('Gaussian Functions G(x)')
#Configuring the grid lines
ax2.grid()

#Sum (with `np.sum()`) all the gaussian functions and normalize the result such that the integral matches the integral of the original histogram.
#For that you could use the `scipy.integrate.trapz()` method. 
#Superimpose the normalized sum of all gaussians to the first histogram.

KDE=np.array(gaussianDistributions).sum(axis=0)

areaUnderIntegral=integrate.trapz(dist, dx=bins[1]-bins[0])

ax1.plot(rangeForgaussianNormalArray,KDE/sum(KDE)*areaUnderIntegral)
plt.show()