x = ['unipd','python','coarse', 'hello' , 'world',"work","padova"]
n= 5
b_list = list(map(lambda i: x[i] , filter(lambda i: len(x[i]) <= n , range(len(x)))))
print(b_list)
