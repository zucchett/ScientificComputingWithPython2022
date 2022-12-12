import pandas as pd
N =69000
df = pd.read_csv('data_000637.txt', sep=',',nrows= N)
df

for i in range (N):
    if df.iloc[i]['BX_COUNTER'] == 0:
        print("The BX counter resets at row: ", i, " Value: ", df.iloc[i]['BX_COUNTER'])
        print("The maximum value before being reset to 0:", df.iloc[i-1]['BX_COUNTER'], "\t Row: ", i-1)
        x = df.iloc[i-1]['BX_COUNTER']
        break
print("x =", x)