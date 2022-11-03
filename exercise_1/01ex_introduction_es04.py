s = input("Insert your text: ")
counter = {}
for i in s :
    if i.isalpha() == True :
        i = i.upper()
        counter[i] = counter.get(i,0) + 1
print(counter)