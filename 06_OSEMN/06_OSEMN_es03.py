!wget https://www.dropbox.com/s/kgshemfgk22iy79/mushrooms_categorized.csv  -P ./data/
import pandas as pd

data = pd.read_csv("data/mushrooms_categorized.csv")
#print(data)

data_means = data.groupby(['class']).mean()
#print(data_means)

data.to_json('data/mushrooms_categorized.json', orient = 'records')