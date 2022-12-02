import pandas as pd   
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
#load the data into dataframe and conver it to pandas dataframe
data=np.load("residuals_261.pkl",allow_pickle=True).item()
data=pd.DataFrame(data)

# Inspection of the dataset
print(data)
print(data.info())