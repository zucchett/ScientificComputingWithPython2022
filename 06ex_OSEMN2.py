import numpy as np
import pandas as pd
import csv
import json    
d = json.load(open('user_data.json'))

header = ["ID","JobTitle","EmailAddress","FirstNameLastName","CreditCard", "CreditCardType"]
l=[]
for a in d:
    if a['CreditCardType'] == 'American Express':
        array= [a["ID"], a["JobTitle"], a["EmailAddress"],a["FirstNameLastName"],a["CreditCard"],a["CreditCardType"]]
        l.append(array)
              

with open('jsonfiltered.csv','w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
    writer.writerow(l) 
          
print("csv file: ")
!cat jsonfiltered.csv 