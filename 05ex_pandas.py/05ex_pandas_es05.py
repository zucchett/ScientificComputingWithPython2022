import numpy as np
import pandas as pd
data = pd.read_csv('data/data_000637.txt')
x=  data.groupby('TDC_CHANNEL').sum().sort_values(by = ['HEAD']).iloc[-3:]
print(x)