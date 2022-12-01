import numpy as np
u=np.array([1,3,5,7])
v=np.array([2,4,6,8])
#section a
print(u)
print(v)
comput=np.outer(u,v)
print(comput)
# section b
a=[]
for i in u:
    b=[]
    for j in v:
        b.append(i*j)
    a.append(b)
print(a)
# section 3
uv=u*v.reshape(4,1)
print(uv.transpose())
