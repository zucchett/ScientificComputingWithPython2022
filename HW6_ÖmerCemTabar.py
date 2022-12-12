"""
Author : Ömer Cem Tabar
Exercise Document 06 Solution File

This file only includes the codes that is required to solve the questions
You can also check the outputs from the notebook

"""

"""
1\. **Text files**

Perform the following operations on plain `txt` files:

+ create a list of integrer numbers and then save it to a text file named `data_int.txt`. Run the `cat` command to print the content of the file.
+ create a matrix of 5x5 floats and then save it to a text file named `data_float.txt`. Use the `cat` command to print the content of the file.
+ load the `txt` file of the previous point and convert it to a `csv` file by hand.

"""
#!wget https://www.dropbox.com/s/sz5klcdpckc39hd/user_data.json -P data/
#!wget https://www.dropbox.com/s/kgshemfgk22iy79/mushrooms_categorized.csv -P data/
#!wget https://www.dropbox.com/s/8m0syw2tkul3dap/credit_card.dat -P data/

import pandas as pd
import numpy as np
import csv
import json # import the JSON module
import pickle
import os
import h5py
from matplotlib import pyplot as plt
from IPython.display import Image
import struct, time

"""
!wget https://www.dropbox.com/s/sz5klcdpckc39hd/user_data.json -P data/
!wget https://www.dropbox.com/s/kgshemfgk22iy79/mushrooms_categorized.csv -P data/
!wget https://www.dropbox.com/s/8m0syw2tkul3dap/credit_card.dat -P data/
"""
import pandas as pd
import numpy as np
import csv
import json # import the JSON module
import pickle
import os
import h5py
from matplotlib import pyplot as plt
from IPython.display import Image
import struct, time

#First bullet point
import random
list_of_numbers = []
for i in range(0, 12):
    number = random.randint(1,543)
    list_of_numbers.append(number)

int_out_file_name = "data/data_int.txt"


with open(int_out_file_name, 'a') as out_int_file:
    for i in range(0,len(list_of_numbers)):
        out_int_file.write(str(list_of_numbers[i])+"\n")

print("Output file reading of data_int.txt:\n")
!cat data_int.txt

#Second bullet point
import numpy.random as npr
float_out_file_name = "data/data_float.txt"
float_matrix = npr.rand(5,5)
with open(float_out_file_name,'a') as out_float_file:
    for row in float_matrix:
        out_float_file.write(str(row)+"\n")

print("Output file reading of data_float.txt:\n")
!cat data_float.txt

#Third bullet point
import csv
with open('data/data_float.txt', 'r') as file:
    strips = []
    for line in file:
        strips.append(line.strip())
    lls = []
    for line in strips:
        ll = []
        splitFirst = line.split(" ")
        sieveFirst = [el for el in splitFirst if el != '']
        ll.append(sieveFirst[0].split("[")[1])
        ll.append(sieveFirst[1])
        ll.append(sieveFirst[2])
        ll.append(sieveFirst[3])
        ll.append(sieveFirst[4].split("]")[0])
        lls.append(ll)
   

    
    with open('data/data_float.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('col1', 'col2', 'col3', 'col4', 'col5'))
        writer.writerows(lls)

"""
2\. **JSON files**

Load the file *user_data.json*, which can be found at:

- https://www.dropbox.com/s/sz5klcdpckc39hd/user_data.json

and filter the data by the "CreditCardType" when it equals to "American Express". Than save the data to a new CSV file.
"""
json_obj = json.load(open('data/user_data.json'))
new_json_array = []
keys = list(json_obj[0].keys())
for i in json_obj:
    if i['CreditCardType'] == 'American Express':
        new_json_array.append(i.values())
        

with open('data/user_data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(keys)
        writer.writerows(new_json_array)


"""
3\. **CSV files with Pandas**

Load the file from this url:

- https://www.dropbox.com/s/kgshemfgk22iy79/mushrooms_categorized.csv

with Pandas. 

+ explore and print the DataFrame
+ calculate, using `groupby()`, the average value of each feature, separately for each class
+ save the file in a JSON format.

"""
import pandas as pd

df = pd.read_csv('data/mushrooms_categorized.csv')
print(df.info())
print(df)

df = df.groupby(['class']).mean()

class0 = df[df.index == 0]
class1 = df[df.index == 1]
keys = list(class0.keys())
d = {}
dclass0 = {}
dclass1 = {}
for element in range(0,len(class0.values[0])):
    dclass0[keys[element]] = class0.values[0][element]
for element in range(0,len(class1.values[0])):
    dclass1[keys[element]] = class0.values[0][element]
d[str(df.index.name)+str(df.index[0])] = dclass0
d[str(df.index.name)+str(df.index[1])] = dclass0   
with open('data/groupby_mushrooms.json', 'w') as f:
    y = json.dumps(d)
    f.write(y)

"""
4\. **Reading the credit card numbers**

Get the binary file named *credit_card.dat* from this address:

- https://www.dropbox.com/s/8m0syw2tkul3dap/credit_card.dat

and convert the data into the real credit card number, knowing that:
- each line corresponds to a credit card number, which consists of 16 characters (which are numbers in the 0-9 range) divided in 4 blocks, with a whitespace between each block
- each character is written using a 6 bit binary representation (including the whitespace)
- the final 4 bits of each line are a padding used to determine the end of the line, and can be ignored

*Hint*: convert the binary numbers to the decimal representation first, and then use the `chr()` function to convert the latter to a char
"""
creditcarddat = "data/credit_card.dat"

with open(creditcarddat, mode = 'r') as f:
    creditCardNumbers = []
    for line in f:
        if len(line[0:114]) == 114:
            creditCardNumbers.append(line[0:114])
    characterRepresentation = []
    for creditCard in creditCardNumbers:
        creditCardString = ""
        for i in range(0,len(creditCard),6):
            binary = creditCard[i:i+6]
            if len(binary) == 6:
                dec = int(binary,2)
                char = chr(dec)
                creditCardString = creditCardString + str(char)
            i = i+6
        characterRepresentation.append(creditCardString)
    print(characterRepresentation)



"""
5\. **Write data to a binary file**

a) Start from the `data/data_000637.txt` file that we have used during the previous lectures, and convert it to a binary file according to the format defined below:


"""
import pandas as pd
import struct, time
file_name = 'data/data_000637.txt'
N = 10
TDC_dataframe = pd.read_csv(file_name, nrows=10)
outputFileName = 'data/binary_file.dat'
with open(outputFileName, 'wb') as binary_file:
    for rows in TDC_dataframe.values:
        #Every rows contains the values under the columns
        word = rows[0] << 62
        word += rows[1] << 58
        word += rows[2] << 49
        word += rows[3] << 17
        word += rows[4] << 5
        word += rows[5] << 0
        binary_file.write(struct.pack('<q',word))
    binary_file.close()

"""
b) Check that the binary file is correctly written by reading it with the code used in the lecture `06_OSEMN.ipynb`, and verify that the content of the `txt` and binary files is consistent.
"""
#Imported warnings since in the future updates df.append will be removed with p.concat
#That is why it gives warning lines
import struct, time, warnings
warnings.filterwarnings("ignore")
data = {}
columns = ['HEAD', 'FPGA', 'CHANNEL', 'ORBIT_CNT', 'BX_CNT', 'TDC_MEAS']
df = pd.DataFrame({}, columns=columns)

with open('data/binary_file.dat', 'rb') as file:
    file_content = file.read()
    word_counter = 0
    word_size = 8 # size of the word in bytes
    for i in range(0, len(file_content), word_size):
        word_counter += 1
        if word_counter > 10: break
        word = struct.unpack('<q', file_content[i : i + word_size])[0] # get an 8-byte word
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

"""
c) What is the difference of the size on disk between equivalent `txt` and binary files?
"""
import os
with open('data/data_000637.txt') as myfile:
    data = [next(myfile) for x in range(11)]

with open('data/data_000637New.txt', 'a') as out_int_file:
    for i in range(0,len(data)):
        out_int_file.write(data[i])

fileNameOne = 'data/data_000637New.txt'
fileNameOneSecond = 'data/binary_file.dat'

firstFileSize = os.path.getsize(fileNameOne)
secondFileSize = os.path.getsize(fileNameOneSecond)

print("The 'data_000637.txt' file with only 10 rows has size: ", str(firstFileSize)," bytes\n")
print("The 'binary_file.dat' file with only 10 rows has size: ", str(secondFileSize)," bytes\n")
print("The difference between the file sizes in bytes: ", str(firstFileSize-secondFileSize))