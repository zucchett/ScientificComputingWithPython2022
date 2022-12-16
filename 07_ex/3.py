#actually, i need more time to underestand this topic, sorry but i miss the deadline, i write this because it is important for me to inform you this lecture is important for me,and i will be solve my problems as soon as possible


import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

data=np.load("residuals_261.pkl",allow_pickle=True).item()
data=pd.DataFrame(data)


print(data)
print(data.info())