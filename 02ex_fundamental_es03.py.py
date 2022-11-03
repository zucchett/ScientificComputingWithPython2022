y = ['nmklj','fdhe','lop', 'lsauh' , 'ksalfw']
n= 4
ans = list(map(lambda i: y[i] , filter(lambda i: len(y[i]) <= n , range(len(y)))))
print(ans)
