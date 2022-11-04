N = 20
var = 5
fac = 1e-1

for i in range(N):
    var = var + fac
    fac = fac * 1e-1
    print(i,"\t\t",var)
    
print("after 14th step there is no effect on the number") 