import pandas as pd   
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

data=np.load("residuals_261.pkl",allow_pickle=True).item()
data=pd.DataFrame(data)


print(data)
print(data.info())