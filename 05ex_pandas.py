# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 16:52:43 2022

@author: 10
"""
#%%
import pandas as pd
import numpy as np
import random

# QUESTION 1
!wget https://www.dropbox.com/s/xvjzaxzz3ysphme/data_000637.txt -P data/
data = pd.read_csv('data/data_000637.txt')
N = (int(1e4) + 1)

data_head = data.head(N)

#%% QUESTION 2
orbit_unit = data_head['BX_COUNTER'].max()

#%% QUESTION 3
counter_bx = np.array(data_head['BX_COUNTER'])
counter_orbit = np.array(data_head['ORBIT_CNT'])
time_ns = (counter_bx+counter_orbit*orbit_unit)*25
data_head['TIME_IN_NS'] = time_ns
time_new = pd.to_datetime(time_ns, unit='ns')
data_head['TIME_SRS'] = time_new

#%% QUESTION 4
import datetime

max_ORBIT_CNT = data_head['ORBIT_CNT'].max()

#%%QUESTION 5

print(data_head[data_head['FPGA'] == 0].groupby(['TDC_CHANNEL']).count()['HEAD'].nlargest(3))
print(data_head[data_head['FPGA'] == 1].groupby(['TDC_CHANNEL']).count()['HEAD'].nlargest(3))

#%% QUESTION 6

non_empty = data_head.loc[data_head['TDC_MEAS']!=0]
print(non_empty.shape[0])
#%%QUESTION 7
channel = data_head.loc[data_head['TDC_CHANNEL'] == 139]
measured = channel.loc[channel['TDC_MEAS'] != 0]
measured.nunique()['ORBIT_CNT']
print(channel.shape[0])

#%% QUESTION 8
fp_0 = data_head.loc[data_head['FPGA'] == 0]
new_series= pd.Series(fp_0['TDC_MEAS'].values,index= fp_0['TDC_CHANNEL'])

fp_1 = data_head.loc[data_head['FPGA'] == 1]
new_series_2= pd.Series(fp_1['TDC_MEAS'].values,index= fp_1['TDC_CHANNEL'])

print(new_series)
print(new_series_2)
