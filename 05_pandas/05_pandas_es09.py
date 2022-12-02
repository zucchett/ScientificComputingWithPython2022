import pandas as pd
N = 35000
data = pd.read_csv('data_000637.txt', header=0, nrows= N, skiprows = 0)

p1 = data.plot.hist(column=["TDC_CHANNEL"], by = "FPGA")
