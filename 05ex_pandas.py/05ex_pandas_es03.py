import numpy as np
import pandas as pd
data = pd.read_csv('data/data_000637.txt')
bx = data["BX_COUNTER"]
estimate_bx = max(bx)
data["abs_time_in_ns"] = data['TDC_MEAS'].transform(lambda x: x * 25/30) + data['BX_COUNTER'].transform(lambda x: x * 25) +data['ORBIT_CNT'].transform(lambda x: x * estimate_bx * 25)
print(data)