import pandas as pd
N = 35000
data = pd.read_csv('data_000637.txt', header=0, nrows= N, skiprows = 0)

df_139 = data[data['TDC_CHANNEL']==139]
print(df_139)
unique_139 = data[data['TDC_CHANNEL']==139]['ORBIT_CNT'].nunique()
print(unique_139)