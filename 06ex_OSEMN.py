# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 22:02:37 2022

@author: 10
"""

import time
import struct
import json
import json  # import the JSON module
import csv
import pandas as pd
import numpy as np

# %% QUESTION 1
import time
import struct
import json
import json  # import the JSON module
import csv
import pandas as pd
import numpy as np


my_list = ['5', '2', '3']

f = open('data_int.txt', 'w')
f.writelines("%s \n" % i for i in my_list)
f.close()

# !cat data_int.txt

array = np.matrix([[1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [
                  1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [1, 2, 3, 4, 5]])
with open('data_int.txt', 'a') as file:
    for line in array:
        np.savetxt(file, line, fmt='%s')

# !cat data_int.txt

# %%QUESTION 2
import time
import struct
import json
import json  # import the JSON module
import csv
import pandas as pd
import numpy as np
!wget https://www.dropbox.com/s/sz5klcdpckc39hd/user_data.json -P data/
data = json.load(open('data/user_data.json'))
data = pd.DataFrame(data)

options = ['American Express']
filtered = data[data['CreditCardType'].isin(options)]
filtered.to_csv(r'new.csv',
                index=False, header=True)

# %% QUESTION 3
import time
import struct
import json
import json  # import the JSON module
import csv
import pandas as pd
import numpy as np
!wget https://www.dropbox.com/s/kgshemfgk22iy79/mushrooms_categorized.csv -P data/
mushroom = pd.read_csv(
    'data/mushrooms_categorized.csv')
average = mushroom.groupby('class').mean()
print(average)
average.to_json('mushroom.json',
                orient='records', lines=True)

# with open('C:/Users/10/OneDrive/Masaüstü/SCP/mushroom.json') as user_file: -> to read
#   file_contents = user_file.read()

# print(file_contents)

# %% QUESTION 4
import time
import struct
import json
import json  # import the JSON module
import csv
import pandas as pd
import numpy as np
!wget https://www.dropbox.com/s/8m0syw2tkul3dap/credit_card.dat -P data/
df_binary = pd.read_csv(
    'data/credit_card.dat', header=None)
card_num = np.array(df_binary)
card_bin = card_num.astype(str)
chars = []
binary_split = []

for j in range(0, len(card_num)):
    binary_split.append([card_num[j][0][i:i + 6]
                        for i in range(0, len(card_num[j][0]), 6)])

for i in range(0, len(binary_split)-1):
    for j in range(0, 20):
        chars.append(((chr(int(binary_split[i][j], 2)))))

credit_num = ''.join(chars)
print(credit_num)

# %% QUESTION 5
import struct, time
import time
import struct
import json
import json  # import the JSON module
import csv
import pandas as pd
import numpy as np
!wget https://www.dropbox.com/s/xvjzaxzz3ysphme/data_000637.txt -P data/
data = pd.read_csv(
    'data/data_000637.txt')
data_head = data.head(10)
head = (packedData>> 62) & 0x3
fpga = (data_head['FPGA'][2] << 58) & 0xF
tdc_chan = (data_head['TDC_CHANNEL'][3] << 49) & 0x1FF
orb_cnt = (data_head['ORBIT_CNT'][3]<< 17) & 0xFFFFFFFF
bx = (data_head['BX_COUNTER'][3] << 5) & 0xFFF
tdc_meas = (data_head['TDC_MEAS'][3] << 0) & 0x1F

struct.pack("@ccc", data_head['BX_COUNTER'][5],data_head['HEAD'][0])
# %% QUESTION 6
import struct, time

packedData = struct.pack('<qqqqqq', data_head['HEAD'][0],data_head['FPGA'][0],data_head['TDC_CHANNEL'][0],data_head['ORBIT_CNT'][0],data_head['BX_COUNTER'][0],data_head['TDC_MEAS'][0])
print(packedData)
un = struct.unpack('qqqqqq',packedData)

