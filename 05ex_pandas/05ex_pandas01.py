import numpy as np
import pandas as pd
from datetime import datetime

data_file = './data_000637.txt'
data = pd.read_csv(data_file)
print("This is the answer of question number 1 :\n", data)

max_bx = data['BX_COUNTER'].max()
print("\nThe answer of question 2 is:\n", max_bx)

data["ABSOLUTE_NS"] = ((data["ORBIT_CNT"] - 3869200167) * (max_bx + 1) * 25) + (data["BX_COUNTER"] * 25) + (data['TDC_MEAS'] * (25/30))
print("\nThis is the answer od question number 3:\n", data)

print("\nThis is the answer of question number 4:\n", pd.Timestamp(data['ABSOLUTE_NS'].iloc[-1]))

print("\nThis is the answer of the question 5: \n",(data.groupby('TDC_CHANNEL').count().sort_values('HEAD')).tail(3)["ORBIT_CNT"])

x = data["ORBIT_CNT"].nunique()
print("\nThis is the answer of the question number 6:\n", x)
x = data[data["TDC_CHANNEL"]== 139]
print("\nThis is the answer of the question nuber 7:\n", x["ORBIT_CNT"].nunique())

x0 = data[data["FPGA"] == 0]
print("\nThis is the answer of question 8 for FPGA = 0:\n", x0.groupby("TDC_CHANNEL").count())
x1 = data[data["FPGA"] == 1]
print("\nThis is the answer of question 8 for FPGA = 1:\n", x1.groupby("TDC_CHANNEL").count())

