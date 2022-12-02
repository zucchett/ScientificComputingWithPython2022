"""
3. CSV files with Pandas
Load the file from this url:
https://www.dropbox.com/s/kgshemfgk22iy79/mushrooms_categorized.csv
with Pandas.
explore and print the DataFrame
calculate, using groupby(), the average value of each feature, separately for each class
save the file in a JSON format.

探索并打印DataFrame
使用groupby()计算每个特征的平均值，分别为每个类。
以JSON格式保存该文件。
"""
import pandas as pd
from os import system
data = pd.read_csv("mushrooms_categorized.csv")
data =data.groupby('class').mean()
print(data)
data.to_json('mushrooms_categorized.json')

system("cat mushrooms_categorized.json")