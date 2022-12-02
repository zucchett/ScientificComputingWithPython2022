import pandas as pd
N = 35000
data = pd.read_csv('data_000637.txt', header=0, nrows= N, skiprows = 0)

s1 = data[data['FPGA']==0].groupby(['TDC_CHANNEL']).size()
s2 = data[data['FPGA']==1].groupby(['TDC_CHANNEL']).size()
print(s1)
print('-----------------------------------------')
print(s2)
