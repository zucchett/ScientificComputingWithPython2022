#!/usr/bin/env python
# coding: utf-8

# Ceren Yilmaz Gulten Exercise 5

# In[31]:


import numpy as np 
import pandas as pd 


# In[82]:


# 1. Pandas Dataframe 
get_ipython().system('wget https://www.dropbox.com/s/xvjzaxzz3ysphme/data_000637.txt -P  data/')
df = pd.read_csv(r"data/data_000637.txt", sep=",") # reading csv file 
df = pd.DataFrame(df)


# In[83]:


# 1.
row = len(df.axes[0])
print("Number of rows:\t",row)
print("Dataframe for N=15000 rows:\n",df.head(15000)) #N=15000 bigger than 10k 
print("Dataframe for maximum number of rows:\n",df.head(row)) # N=row number(1310720)
df = df.head(15000)


# In[84]:


# 2. 
data = df.loc[df['BX_COUNTER'] == 0] # values where BX_Counter is equals 0 
print(data)
bx_counter = df.head(2894) # first index of BX_Counter is zero is 2894 we can get the data until 2894th line 
x = bx_counter['BX_COUNTER'].max() # get the maximum value from the selected dataset 
print('x=',x)


# In[128]:


# 3. 
bx = np.array(df['BX_COUNTER'])
orbit = np.array(df['ORBIT_CNT'])
ns  = (bx+orbit*x)*25
df['TIME'] = ns
ns_series = pd.to_datetime(ns,unit='ns')
df['TIME_SERIES'] = ns_series
print(df)


# In[79]:


#4. 


# In[74]:


# 5. 
print('FPGA == 1\n',df[df['FPGA'] == 1].groupby(['TDC_CHANNEL']).count()['FPGA'].nlargest(3))
print('FPGA == 0\n',df[df['FPGA'] == 0].groupby(['TDC_CHANNEL']).count()['FPGA'].nlargest(3))


# In[85]:


# 6. 

nonempty_orbit = df.loc[df['TDC_MEAS'] != 0] # TDC_MEAS is shows if measurement is done  
print("Number of non empty orbit: " , nonempty_orbit.shape[0])


# In[86]:


# 7. 

tdc_139 = df.loc[df['TDC_CHANNEL']==139 ] # the data where TDC_CHANNEL==139
uniq=tdc_139['ORBIT_CNT'].unique() # take the unique values for ORBIT_CNT from defined dataset
print("Number of unique orbit for TDC_CHANNEL == 139: ",uniq.shape[0]) # shape for count the number


# In[124]:


# 8. 
fpga_zero = df.loc[df['FPGA'] == 0]
fpga_one = df.loc[df['FPGA'] == 1]
fpga_zero_tdc = pd.Series(fpga_zero['TDC_MEAS'].values, index= fpga_zero['TDC_CHANNEL'])
fpga_one_tdc = pd.Series(fpga_one['TDC_MEAS'].values, index= fpga_one['TDC_CHANNEL'])
print(fpga_zero_tdc)
print(fpga_one_tdc)

