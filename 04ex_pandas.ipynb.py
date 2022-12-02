import pandas as pd

N=69000
df = pd.read_csv('data_000637.txt', sep=',',nrows=N)
df

df['DURATION_MEASUREMENT'] = pd.to_timedelta(df['ABSOLUTE_TIME'])
print("The duration of each measurement:", df['DURATION_MEASUREMENT'][0:5].diff())
print("The duration of the whole data taking:", (df['DURATION_MEASUREMENT'].max() - df['DURATION_MEASUREMENT'].min()))