import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
data = pd.read_csv("./regression_generated.csv")
print(data.columns)
reduced_data = data[["features_1", "features_2", "features_3"]]
sb.pairplot(reduced_data)
plt.show()
# All the features are almost the same, and they are generated with the same std and mean
