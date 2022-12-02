import datetime as dt
import pandas as pd
N = 35000
data = pd.read_csv('data_000637.txt', header=0, nrows= N, skiprows = 0)


itime = dt.datetime.now()
print("Begin time:", itime)

# the one-liner command
time =  data['TDC_MEAS'] *(25/30) + data['BX_COUNTER'] * 25 + data['ORBIT_CNT']*estimated_bx*25

ftime = dt.datetime.now()
print("End time:", ftime)
print("Elapsed time:", (ftime - itime))