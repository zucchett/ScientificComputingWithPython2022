import pandas as pd
N=69000
df = pd.read_csv('data_000637.txt', sep=',',nrows=N)
df
df.describe()

