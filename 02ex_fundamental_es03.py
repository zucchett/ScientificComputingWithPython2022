x = ['hgfkhkfhkldhk','hdij','njkmn', 'sannj' , 'sra']
n = 4
num= list(map(lambda i: x[i] , filter(lambda i: len(x[i]) <= n , range(len(x)))))
print(num)