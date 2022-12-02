
import pandas as pd
N = 69000
df = pd.read_csv('data_000637.txt', sep=',',nrows=N)
df
df = df.assign(ABSOLUTE_TIME=df['BX_COUNTER'] + df['TDC_MEAS'] +df['ORBIT_CNT'])
df/10**9