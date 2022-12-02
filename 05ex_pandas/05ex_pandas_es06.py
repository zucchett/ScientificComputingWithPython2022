"""
6. Count the number of non-empty orbits (i.e. the number of orbits with at least one hit).
6. 计算非空轨道的数量（即至少有一个命中的轨道的数量）。
"""
import pandas as pd

N = 1000000
df = pd.read_csv('data/data_000637.txt', nrows=N)
non_empty_orbits = df.groupby('ORBIT_CNT')
print("Number of non-empty orbits: ", len(non_empty_orbits))
