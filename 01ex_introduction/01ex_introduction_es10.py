#10.Normalization of a N-dimensional vector

import math
def Norm(T):
    y=()
    x=()
    for i in range(len(T)):
        x=x+(T[i]**2,) #(4, 9, 16, 36)
    for i in range(len(T)):
        s=math.sqrt(sum(x))
        y=y+(T[i]/s,)
    return y
T=(2,3,4,6)
x=Norm(T)
s=()
for i in range(len(x)):
        s=s+(x[i]**2,)
print(sum(s))

