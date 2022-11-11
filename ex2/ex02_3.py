N = int(input('please insert the value of N: '))
firstlist = ['a','b','c','d']
flist = list(filter(lambda n : len(n)<N , firstlist))
print(flist)