import numpy as np
import os
import pandas as pd

file1 = open('data/data_int.txt', 'a+')
int_numbers = np.arange(1,21)
for i in int_numbers:
    file1.write(str(i) + '\n')

file2 = open('data/data_float.txt', 'a+')
float_numbers = np.arange(1,26, dtype = float).reshape(5,5)
for i in float_numbers:
    file2.write(str(i)+'\n')

