import pandas as pd
N=69000
df = pd.read_csv('data_000637.txt', sep=',',nrows=N)
df
print(" The top 3 TDC_CHANNELS: ", df.groupby('HEAD')['TDC_CHANNEL'].nlargest(3))