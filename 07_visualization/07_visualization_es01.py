!wget "https://www.dropbox.com/s/aamg1apjhclecka/regression_generated.csv" -P ./data/
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/regression_generated.csv")
scatter_plots = pd.plotting.scatter_matrix(data[['features_1','features_2', 'features_3']],figsize=(8,6), c="b", grid='True')

correlations = data[['features_1','features_2', 'features_3']].corr()
print(correlations)

# As it is shown in correlation matrix, these features are NOT correlated.