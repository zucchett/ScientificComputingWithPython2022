import datetime as dt
import numpy as np
import pandas as pd
data = pd.read_csv('data/data_000637.txt')
begin_time = dt.datetime.now()
print(begin_time)
time = data['TDC_MEAS'] *(25/30) + data['BX_COUNTER'] * 25 + data['ORBIT_CNT']*est_bx*25
end_time = dt.datetime.now()
print(end_time)
print((end_time - begin_time))