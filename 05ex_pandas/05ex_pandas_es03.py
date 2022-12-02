"""
3. Create a new column with the absolute time in ns (as a combination of the other three columns with timing
information) since the beginning of the data acquisition, and convert the new column to a Time Series.
3.  创建一个新的列，包含自数据采集开始以来的绝对时间（以ns为单位）（作为其他三个列的时间信息的组合 信息的组合），并将新列转换为时间序列
"""
import pandas as pd

N = 1000000
df = pd.read_csv('data/data_000637.txt', nrows=N)
max_bx = df['BX_COUNTER'].max() + 1

max_tdc = max(df["TDC_MEAS"]) + 1

bx_with_max_orbit = df.loc[df['ORBIT_CNT'] == max(df["ORBIT_CNT"])]
bx_with_min_orbit = df.loc[df['ORBIT_CNT'] == min(df["ORBIT_CNT"])]

tdc_with_min_bx = bx_with_min_orbit.loc[bx_with_min_orbit['BX_COUNTER'] == min(bx_with_min_orbit["BX_COUNTER"])]

initial_ns = (min(df["ORBIT_CNT"])*max_bx + min(bx_with_min_orbit["BX_COUNTER"])) * 25 + min(tdc_with_min_bx["TDC_MEAS"]) * 25/30
df['NS_PASSED'] = ((df['ORBIT_CNT']*max_bx + df['BX_COUNTER']) * 25 + df['TDC_MEAS']*25/30) - initial_ns
df