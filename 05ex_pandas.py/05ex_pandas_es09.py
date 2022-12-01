import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv 
data = pd.read_csv('data/data_000637.txt')
FPGA_0 = pd.Series(data[data['FPGA'] == 0]['TDC_CHANNEL'].value_counts())
FPGA_1 = pd.Series(data[data['FPGA'] == 1]['TDC_CHANNEL'].value_counts())
plt.hist(FPGA_0)
plt.title('FPGA == 0')
plt.xlabel('TDC_CHANNEL')
plt.ylabel('number of counts')
plt.show()
plt.hist(FPGA_1)
plt.title('FPGA == 1')
plt.xlabel('TDC_CHANNEL')
plt.ylabel('number of counts')
plt.show()