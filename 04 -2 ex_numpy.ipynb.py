u = np.array([1, 3, 5, 7])
v= np.array([2, 4, 6, 8])

#1 Using the function outer in numpy
SU = np.outer(u,v)
print(SU,"\n")
#2 Using a nested for loop
SH= []
for i in u:
    row = []
    for j in v:
        row.append(i * j)
    SH.append(row)
print(SH,"\n")
#3 Using numpy broadcasting operations
u_v =u * v.reshape(4,1)
print(u_v.transpose())