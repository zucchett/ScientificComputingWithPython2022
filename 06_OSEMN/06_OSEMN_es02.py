!wget https://www.dropbox.com/s/sz5klcdpckc39hd/user_data.json  -P ./data/
import json
import csv

with open("data/user_data.json") as f:
    users = json.load(f)

keys = users[0].keys()
header = list(keys)

filtered_users = []
for user in users:
    if user['CreditCardType'] == 'American Express':
        a = []
        for key in keys:
            a.append(user[key])
        filtered_users.append(a)
        
with open('data/filtered_users.csv','w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for a in filtered_users:
        writer.writerow(a)

!cat "data/filtered_users.csv"