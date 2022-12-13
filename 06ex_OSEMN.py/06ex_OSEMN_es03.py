import numpy as np
import pandas as pd
import json
#section a , b
data = pd.read_csv("mushrooms_categorized.csv") 
cal = data.groupby('class')
class0 = cal.get_group(0)   
mean_class0 = class0.mean()
print(mean_class0)
mean_class0_json0 = mean_class0.to_json()

class1 = cal.get_group(1)   
mean_class1 = class1.mean()
print(mean_class1)         
mean_class1_json1 = mean_class1.to_json()
#section c 
jsonString0 = json.dumps(mean_class0_json0)
jsonFile0 = open("mean_class0_json1.json", "w")
jsonFile0.write(jsonString0)
jsonFile0.close()

jsonString = json.dumps(mean_class1_json1)
jsonFile = open("mean_class1_json1.json", "w")
jsonFile.write(jsonString)
jsonFile.close()