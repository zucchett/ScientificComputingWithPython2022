import pandas as pd
import json as js

path = 'data/json_output.csv'
data = pd.read_json("data/user_data.json")
filtered_data = data[data["CreditCardType"]== "American Express"]
print("This is the filtered data:\n", filtered_data)
filtered_data.to_csv(path)
