x = ['ICT' , 'Python' , 'Javascript' , 'Json' , 'Hi' , 'Cplusplus' , 'Sina' ]
n= 5
ans = list(map(lambda i: x[i] , filter(lambda i: len(x[i]) <= n , range(len(x)))))
print(ans)
