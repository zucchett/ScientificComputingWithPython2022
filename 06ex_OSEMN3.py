import numpy as np
import pandas as pd
import csv

file_1 = "mushrooms_categorized.csv"
data_1 = pd.read_csv(file_1)


gb = data_1.groupby(['class']).mean()

data_frame = pd.DataFrame(gb)

data_frame.to_json(r'./export_mean_json.json', orient = 'index')