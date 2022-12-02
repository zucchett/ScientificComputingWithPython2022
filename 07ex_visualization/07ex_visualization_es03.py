"""
3. Profile plot

Produce a profile plot from a scatter plot.

Download the following pickle file:
wget https://www.dropbox.com/s/3uqleyc3wyz52tr/residuals_261.pkl -P data/
Inspect the dataset, you'll find two variables (features)
Convert the content to a Pandas Dataframe
Clean the sample by selecting the entries (rows) with the absolute values of the variable "residual" smaller than 2
Plot a Seaborn jointplot of "residuals" versus "distances", and use seaborn to display a linear regression.
Comment on the correlation between these variables.

Create manually (without using seaborn) the profile histogram for the "distance" variable; choose an appropriate binning.
Obtain 3 numpy arrays:
x, the array of bin centers of the profile histogram of the "distance" variable
y, the mean values of the "residuals", estimated in slices (bins) of "distance"
err_y, the standard deviation of the "residuals", estimated in slices (bins) of "distance"
Plot the profile plot on top of the scatter plot
"""

import pandas as pd
import seaborn as sns

data = pd.read_pickle('residuals_261.pkl')
data_dictionary = data[()]

df = pd.DataFrame(data_dictionary)
print(df)

#Clean the sample
df_clean = df[df['residuals'].abs() < 2]


plot = sns.jointplot(x="distances", y="residuals", data=df_clean, kind="reg", color = "r" ,line_kws = {"color": "w"});
plot.set_axis_labels("Distances", "Residuals")
