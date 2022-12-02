#!/usr/bin/env python
# coding: utf-8

# Ceren Yılmaz Gülten Exercise 6

# In[1]:


import numpy as np 
import pandas as pd
import json
import csv


# In[5]:


# 1. Text Files 
import random 
num = []
for i in range(10):
    num.append(str(random.randint(1,25)))
with open('data_int.txt', 'w') as f:
    for nums in num:
        f.write(nums)
        f.write('\n')
        
#!cat data_int.txt
numbers=[]
# random number generate and append to list
for i in range(28):
    numbers.append(str(round(random.uniform(1.2,35.6),2)))
# create empty array 
matrix = np.empty((5,5),float)
m = 0
for k in range(5):
    for j in range(5):
        matrix[k][j] = numbers[m]
        m +=1
matrix_s = str(matrix)
with open('data_float.txt', 'w') as f:
        for floats in matrix:
            f.write(" ".join([str(n) for n in floats]) + "\n") # to remove [] part
#!cat data_float.txt 
float_txt = np.loadtxt('data_float.txt')
float_txt = pd.read_csv('data_float.txt')
float_txt.to_csv('data_float.csv', index=None)


# In[7]:


# 2. JSON Files 
# load the dataset
get_ipython().system('wget https://www.dropbox.com/s/sz5klcdpckc39hd/user_data.json -P data/')
data = json.load(open('data/user_data.json'))
df = pd.DataFrame(data)
# filtering the data based on creditcardtype
americanexpress = df.loc[df['CreditCardType']== 'American Express']
print(americanexpress)
# Create csv file for American Express Card Type 
americanexpress.to_csv('americanexpress.csv', index =False)  


# In[8]:


# 3. CSV Files with Pandas 
import json
# reading the data and explore dataframe 
get_ipython().system('wget https://www.dropbox.com/s/kgshemfgk22iy79/mushrooms_categorized.csv -P data/')
data = pd.read_csv('data/mushrooms_categorized.csv')
df = pd.DataFrame(data)
print(df)

new_data = {} # for json data
head = [] # for header list 
j = 1
# getting the headers for json file 
for i in df:
    if i == "class":
        head.append(i)
    else:
        head.append(i + "-mean")
# getting each properties mean except class property using groupby property 
for i in df:
    if i == "class":
        continue
    else:
        mean = df.groupby("class")[i].mean() # grouped with groupby and found mean each property based on class value 0 and 1
        new = dict(mean) # convert to dictionary to adding json file 
        new_data[head[j]] = new # adding mean result to each responsible header 
    j += 1           
# open and write into json file 
with open("mean.json", 'w') as jsonFile:
    # adding data to json file 
    z = jsonFile.write(json.dumps(new_data))


# In[9]:


# 4. Reading the credit card numbers
# read data as a csv to get data clear
get_ipython().system('wget https://www.dropbox.com/s/8m0syw2tkul3dap/credit_card.dat -P data/')
card_number_file = pd.read_csv("data/credit_card.dat", header=None)
card_number = []
convert = ""
each_ch_dec = []
# put each line (each card number) to array and it get data as a string 
for i in range(card_number_file.shape[0]):
    card_number.append(card_number_file[0][i])
# define start points
a = 0 
b = 6
for j,i in zip(range(len(card_number)+1),range(len(card_number))): #for loop for operate each line 
    for a,b in zip(range(0,len(card_number[i])+1,6),range(6,123,6)): # get the binary numbers as a 6 bit block for each line
        convert+=card_number[j][a:b] # add to the each 6 bit block to a empty string
        each_ch_dec.append(chr(int(convert,2))) # to convert 6 bit binary number to decimal first convert to int and after char
        # and append the each decimal value to empty list
        convert = "" # clear the convert string for next 6 bit binary block 
#print(each_ch_dec)
credit_num = ''.join(each_ch_dec)  # combine the list values to get proper result
print(credit_num)
#print(len(card_number))       


# In[13]:


# 5.
import struct
get_ipython().system('wget https://www.dropbox.com/s/xvjzaxzz3ysphme/data_000637.txt -P data/')
df = pd.read_csv(r"data/data_000637.txt", sep=",", nrows=10)
df = pd.DataFrame(df)
print(df)

head = (df['HEAD'][0] >> 0) & 0x3
fpga = (df['FPGA'][0] >> 2) & 0xF
tdc_c = (df['TDC_CHANNEL'][0] >> 6) & 0x1FF
orbit_cn = (df['ORBIT_CNT'][0] >> 15) & 0xFFFFFFFF
bx_co = (df['BX_COUNTER'][0] >> 47) & 0xFFF
#tdc_m =(a >> 59) & 0x1F
a = df['TDC_MEAS'][0]
print(type(a))
print(tdc_m)
#for index, row in df.iterrows():


# In[47]:


import struct, time

data = {}
columns = ['HEAD', 'FPGA', 'CHANNEL', 'ORBIT_CNT', 'BX_CNT', 'TDC_MEAS']
df = pd.DataFrame({}, columns=columns)

with open('data_000637.dat', 'rb') as file:
    file_content = file.read()
    word_counter = 0
    word_size = 8 # size of the word in bytes
    for i in range(0, len(file_content), word_size):
        word_counter += 1
        if word_counter > 10: break
        word = struct.unpack('“,file_content[i : i + word_size])[0] 
        head     = (word >> 62) & 0x3
        fpga     = (word >> 58) & 0xF
        tdc_chan = (word >> 49) & 0x1FF
        orb_cnt  = (word >> 17) & 0xFFFFFFFF
        bx       = (word >> 5 ) & 0xFFF
        tdc_meas = (word >> 0 ) & 0x1F
        #if i == 0: print ('{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format('HEAD', 'FPGA', 'CHANNEL', 'ORBIT_CNT', 'BX_CNT', 'TDC_MEAS'))
        #print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(head, fpga, tdc_chan, orb_cnt, bx, tdc_meas))
        entry = {'HEAD' : head, 'FPGA' : fpga, 'CHANNEL' : tdc_chan, 'ORBIT_CNT' : orb_cnt, 'BX_CNT' : bx, 'TDC_MEAS' : tdc_meas}
        df = df.append(entry, ignore_index=True)

df
                             
”


# In[46]:


get_ipython().system('hexdump data_000637.dat')

