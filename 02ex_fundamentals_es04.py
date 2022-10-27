lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
b = []
for i in lang:
    b.append(i)
a = []

r = list(map(lambda x : a.append(len(x)) , b))

print(a)