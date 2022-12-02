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
data = pd.read_csv("regression_generated.csv")
print(data)