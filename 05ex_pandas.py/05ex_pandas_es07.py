import numpy as np
import pandas as pd
data = pd.read_csv('data/data_000637.txt')
unique_orbits = pd.DataFrame(data[data['TDC_CHANNEL'] == 139]).drop_duplicates(subset=['ORBIT_CNT'], inplace=False)
print(len(unique_orbits))
