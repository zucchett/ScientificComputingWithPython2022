import numpy as np
import pandas as pd
import csv  
import json 
data = json.load(open('user_data.json'))
b= []

heads = ["CreditCardType","ID","JobTitle","EmailAddress","FirstNameLastName","CreditCard"]

for i in range (len(data)):
    if data[i]["CreditCardType"] == "American Express":
        print(format(data[i]["CreditCardType"],data[i]["ID"],data[i]["JobTitle"],data[i]["EmailAddress"],data[i]["FirstNameLastName"],data[i]["CreditCard"]))
        array = [data[i]["CreditCardType"],data[i]["ID"],data[i]["JobTitle"],data[i]["EmailAddress"],data[i]["FirstNameLastName"],data[i]["CreditCard"]]
        b.append(array)
        b.append("\n")

with open('new_user_data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(heads)
    writer.writerow(b)