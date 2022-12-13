import numpy as np
import pandas as pd
data = pd.read_csv('data/data_000637.txt')
count_num = data.ORBIT_CNT.unique().size
print(str(count_num))