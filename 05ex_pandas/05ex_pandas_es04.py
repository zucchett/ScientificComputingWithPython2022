"""
4. Find out the duration of the data taking in hours, minutes and seconds, by using the features
of the Time Series. Perform this check reading the whole dataset.
4. 利用时间序列的特点，找出以小时、分钟和秒为单位的数据持续时间。时间序列的特征。对整个数据集进行这一检查。
"""
#and the timing information ('ORBIT_CNT', 'BX_COUNTER', and 'TDC_MEAS')
import pandas as pd

N = 1000000
df = pd.read_csv('data/data_000637.txt', nrows=N)
max_bx = df['BX_COUNTER'].max() + 1

max_tdc = max(df["TDC_MEAS"]) + 1

dif_orbit = max(df["ORBIT_CNT"]) - min(df["ORBIT_CNT"])

bx_with_max_orbit = df.loc[df['ORBIT_CNT'] == max(df["ORBIT_CNT"])]
bx_with_min_orbit = df.loc[df['ORBIT_CNT'] == min(df["ORBIT_CNT"])]

dif_bx = max(bx_with_max_orbit["BX_COUNTER"]) - min(bx_with_min_orbit["BX_COUNTER"])

tdc_with_max_bx = bx_with_max_orbit.loc[bx_with_max_orbit['BX_COUNTER'] == max(bx_with_max_orbit["BX_COUNTER"])]
tdc_with_min_bx = bx_with_min_orbit.loc[bx_with_min_orbit['BX_COUNTER'] == min(bx_with_min_orbit["BX_COUNTER"])]

dif_tdc = max(tdc_with_max_bx["TDC_MEAS"]) - min(tdc_with_min_bx["TDC_MEAS"])

if dif_tdc < 0:
    dif_bx = dif_bx - 1
    dif_tdc = dif_tdc + max_tdc

print(dif_orbit, " orbit ")
print(dif_bx, " bx")
print(dif_tdc, " tdc")

print(((dif_orbit*max_bx)+dif_bx)*25*1e-9 + dif_tdc * 25/30*1e-9, " seconds")
