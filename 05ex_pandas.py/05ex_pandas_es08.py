import numpy as np
import pandas as pd
data = pd.read_csv('data/data_000637.txt')
FPGA_0 = pd.Series(data[data['FPGA'] == 0]['TDC_CHANNEL'].value_counts())
FPGA_1 = pd.Series(data[data['FPGA'] == 1]['TDC_CHANNEL'].value_counts())
print(FPGA_0)
print(FPGA_1)