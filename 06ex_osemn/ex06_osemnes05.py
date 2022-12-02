import pandas as pd
import struct

data = pd.read_csv("data/data_000637.txt")
output = open("data/data_000637.dat", "wb")
data = data[0:10]
for i, r in data.iterrows():
    shifted_data = r["TDC_MEAS"]
    shifted_data += r["BX_COUNTER"] << 5
    shifted_data += r["ORBIT_CNT"] << 17
    shifted_data += r["TDC_CHANNEL"] << 49
    shifted_data += r["FPGA"] << 58
    shifted_data += r["HEAD"] << 62
    output.write(struct.pack("<q", shifted_data))
# The size of the binary file is too much less than the text file
# 10M data/data_000637.dat
# 32M data/data_000637.txt

