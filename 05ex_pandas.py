import pandas as pd
import matplotlib.pyplot as plt
#  1. Create a Pandas DataFrame reading N rows of the data/data_000637.txt dataset.
#  Choose N to be smaller than or equal to the maximum number of rows and larger that 10k (check the documentation).
pd.set_option('display.max_rows', None)
df = pd.read_csv('data_000637.txt')
N = 20000
print(df.head(N))
# number of rows = 1310720
# N = 12k
# 2. Estimate the number of BX in a ORBIT (the value x).
for i in range (N):
    if df.iloc[i]['BX_COUNTER'] == 0:
        print("\nThe BX counter resets at row: ", i, "\t Value: ", df.iloc[i]['BX_COUNTER'])
        print("\nThe maximum value before being reset to 0:", df.iloc[i-1]['BX_COUNTER'], "\t Row: ", i-1)
        x = df.iloc[i-1]['BX_COUNTER']
        break
print("\nx =", x)
# 3. Create a new column with the absolute time in ns (as a combination of the other three columns
# with timing information) since the beginning of the data acquisition, and convert the new column to a Time Series.
df = df.assign(ABSOLUTE_TIME=df['BX_COUNTER'].apply(lambda x: x*25) + df['TDC_MEAS'].apply(lambda x: x*25/30) +
                      df['ORBIT_CNT'].apply(lambda x: x*25*3563))
print("\nThe new column:\n", df['ABSOLUTE_TIME'][0:10])
# 4. Find out the duration of the data taking in hours, minutes and seconds, by using the features of the Time Series.
# Perform this check reading the whole dataset.
df['DURATION_MEASUREMENT'] = pd.to_timedelta(df['ABSOLUTE_TIME'])
print("\nThe duration of each measurement:\n", df['DURATION_MEASUREMENT'][0:5].diff())
print("\nThe duration of the whole data taking:\n", (df['DURATION_MEASUREMENT'].max() - df['DURATION_MEASUREMENT'].min()))
# 5. Use the groupby() method to find out the noisy channels, i.e. the TDC channels with most counts
# print to screen the top 3 and the corresponding counts)
print("\n The top 3 TDC_CHANNELS: ", df.groupby('HEAD')['TDC_CHANNEL'].nlargest(3))
# 6. Count the number of non-empty orbits (i.e. the number of orbits with at least one hit).
count = df.ORBIT_CNT.unique().size
print("The number of orbits with at least one hit is " + str(count))
# 7. Count the number of unique orbits with at least one measurement from TDC_CHANNEL=139.
unique_orbits = pd.DataFrame(df[df['TDC_CHANNEL'] == 139]).drop_duplicates(subset=['ORBIT_CNT'], inplace=False)
print("\nThe number of unique orbits with at least one measurement from TDC_CHANNEL = 139 is ", len(unique_orbits))
# 8. Create two Series (one for each FPGA) that have the TDC channel as index, and the number of counts for the
# corresponding TDC channel as values.
FPGA_0 = pd.Series(df[df['FPGA'] == 0]['TDC_CHANNEL'].value_counts())
FPGA_1 = pd.Series(df[df['FPGA'] == 1]['TDC_CHANNEL'].value_counts())
print("Series 1:", FPGA_0)
print("\nSeries 2", FPGA_1)
# 9. Optional: Create two histograms (one for each FPGA) that show the number of counts for each TDC channel.
plt.hist(FPGA_0)
plt.title('FPGA 0')
plt.xlabel('TDC_CHANNEL')
plt.ylabel('Number of counts')
plt.show()
print("\n")
plt.hist(FPGA_1)
plt.title('FPGA 1')
plt.xlabel('TDC_CHANNEL')
plt.ylabel('Number of counts')
plt.show()






