a = 1.0
for i in range(0,1030):
    a = a * 2
    if (i > 1000):
        print("i :",i," |||  a :",a)

# As it is shown below (after run), "a : 8.98846567431158e+307 (i:1022)" is overflow.

print("-------------------------")
b = 1.0
for i in range(0,1080):
    b = b / 2
    if (i > 1050):
        print("i :",i," |||  b :",b)
        
# As it is shown below (after run), "b : 5e-324 (i:1073)" is underflow.