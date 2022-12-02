import numpy as np
import pandas as pd
import struct

#a
N = 10
data = pd.read_csv('data_000637.txt', header=0, nrows= N, skiprows = 0)
#print(data)
word_size = 8
print(data)
with open('data/new_binary_data.dat', 'wb') as file:
    for row in data.iterrows():
        word  = 0
        word = word | row[1]['HEAD']
        word = (word << 4) | row[1]['FPGA']
        word = (word << 9) | row[1]['TDC_CHANNEL']
        word = (word << 32) | row[1]['ORBIT_CNT']
        word = (word << 12) | row[1]['BX_COUNTER']
        word = (word << 5) | row[1]['TDC_MEAS']
        packed = struct.pack('<q', word) # get an 8-byte word
        file.write(packed)
file.close()

#b
data = {}
columns = ['HEAD', 'FPGA', 'CHANNEL', 'ORBIT_CNT', 'BX_CNT', 'TDC_MEAS']
df = pd.DataFrame({}, columns=columns)

with open('data/new_binary_data.dat', 'rb') as file:
    file_content = file.read()
    word_counter = 0
    word_size = 8 # size of the word in bytes
    for i in range(0, len(file_content), word_size):
        word_counter += 1
        if word_counter > 10: break
        word = struct.unpack('q', file_content[i : i + word_size])[0] # get an 8-byte word
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
print(df)



#c
# Size of a TEXT file containing 10 first rows of mentioned dataset is 295 bytes.
# Size of a BINARY file containing exact same data is 80 bytes.
# Storing data in binary format needs so much less storage.