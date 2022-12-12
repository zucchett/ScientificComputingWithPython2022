import pandas as pd
N=69000
df = pd.read_csv('data_000637.txt', sep=',',nrows=N)
df
unique_orbits = pd.DataFrame(df[df['TDC_CHANNEL'] == 139]).drop_duplicates(subset=['ORBIT_CNT'], inplace=False)
print("\nThe number of unique orbits with at least one measurement from TDC_CHANNEL = 139 is ", len(unique_orbits))