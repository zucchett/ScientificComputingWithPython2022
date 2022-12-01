import pandas as pd
import numpy as np
import csv 

data = pd.read_csv('data/data_000637.txt')
print(data.head(1200)) 
print(data.info()) 