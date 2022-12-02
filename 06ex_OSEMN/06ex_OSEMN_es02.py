"""
2. JSON files
Load the file user_data.json, which can be found at:
https://www.dropbox.com/s/sz5klcdpckc39hd/user_data.json
and filter the data by the "CreditCardType" when it equals to "American Express". Than save the data to a new CSV file.

加载文件user_data.json，该文件可以在以下位置找到。
https://www.dropbox.com/s/sz5klcdpckc39hd/user_data.json
并通过 "CreditCardType "过滤数据，当它等于 "American Express "时。然后将数据保存到一个新的CSV文件中。
"""
import pandas as pd
file = pd.read_json("user_data.json")
print(file)
file = file[(file['CreditCardType'] == "American Express")]
print(file)