"""
7. Count the number of unique orbits with at least one measurement from TDC_CHANNEL=139.
计算至少有一个来自TDC_CHANNEL=139的测量值的独特轨道的数量。
"""
import pandas as pd

N = 1000000
df = pd.read_csv('data/data_000637.txt', nrows=N)
tdc_channel_139 = df[df['TDC_CHANNEL'] == 139].groupby('ORBIT_CNT')
print("Number of unique orbits where TDC_CHANNEL is equal to 139: ", len(tdc_channel_139))