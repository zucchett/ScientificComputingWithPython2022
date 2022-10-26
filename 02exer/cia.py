value = int(input())
list = [5,10,15,20]

found = False
for i in list:
    if i == value:
        found = True
        break

if found:
    print("Value is in list.")
else:
    print("Value is not in list.")