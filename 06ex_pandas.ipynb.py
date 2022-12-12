import pandas as pd
N=69000
df = pd.read_csv('data_000637.txt', sep=',',nrows=N)
df
count = df.ORBIT_CNT.unique().size
print("The number of orbits with at least one hit is " + str(count))