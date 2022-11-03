x = ['Shirin','Mohajeri','Shima', 'Armaghan' , 'ICT',"Abdi","maryam"]
n= 6
rng = list(map(lambda i: x[i] , filter(lambda i: len(x[i]) <= n , range(len(x)))))
print(rng)
