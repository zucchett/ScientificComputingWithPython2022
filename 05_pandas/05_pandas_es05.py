import pandas as pd
N = 35000
data = pd.read_csv('data_000637.txt', header=0, nrows= N, skiprows = 0)
a = data.groupby(['TDC_CHANNEL']).size().sort_values().iloc[-3:]
a