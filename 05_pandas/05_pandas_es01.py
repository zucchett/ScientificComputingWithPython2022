import pandas as pd

N = 35000
data = pd.read_csv('data_000637.txt', header=0, nrows= N, skiprows = 0)
data