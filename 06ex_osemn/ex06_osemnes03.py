import pandas as pd
file = '../data/mushrooms_categorized.csv'
data = pd.read_csv(file)
print("This is the main csv file:/n", data)
data = data.groupby("class").mean()
print("\nThis is the classefied data:/n", data)
json_data = data.to_json('../data/mushrooms_classified_mean.json')

