import pandas as pd
N = 35000
data = pd.read_csv('data_000637.txt', header=0, nrows= N, skiprows = 0)

data['ABSOLUTE_TIME_NS'] = (data['ORBIT_CNT'] * x + data['BX_COUNTER']) * 25 + data['TDC_MEAS']* 25/30
data['ABSOLUTE_TIME_NS'] = data['ABSOLUTE_TIME_NS'] - min(data['ABSOLUTE_TIME_NS'])
data['ABSOLUTE_TIME_SERIES'] = pd.to_datetime(data['ABSOLUTE_TIME_NS'], unit = 'ns')
data