"""
5. Use the .groupby() method to find out the noisy channels, i.e. the TDC channels with most
counts (print to screen the top 3 and the corresponding counts)
5:使用.groupby()方法找出噪声通道，即计数最多的TDC通道（在屏幕上打印出前三名和相应的计数）。
"""
import pandas as pd

N = 1000000
df = pd.read_csv('data/data_000637.txt', nrows=N)
max_bx = df['BX_COUNTER'].max() + 1
noisy_channels = df.groupby(by=["TDC_CHANNEL"]).size().sort_values(ascending = False).head(3)
