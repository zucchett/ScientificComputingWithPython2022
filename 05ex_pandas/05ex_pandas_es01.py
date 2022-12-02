"""
1. Create a Pandas DataFrame reading N rows of the data/data_000637.txt dataset. Choose N to be smaller than
or equal to the maximum number of rows and larger that 10k (check the documentation).
1. 创建一个Pandas DataFrame，读取data/data_000637.txt数据集的N行。选择N要小于或等于最大行数，并且大于10k（查看文档）。
"""
import pandas as pd
from IPython.display import display

N = 1000000
df = pd.read_csv('data/data_000637.txt', nrows=N)
print(df)
