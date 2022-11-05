N = 25
var = 13
fac = 1e-3

for i in range(N):
    var = var + fac
    fac = fac * 1e-1
    print(i,"\t\t",var)
    
print("after 12th step there is no effect on the number") 