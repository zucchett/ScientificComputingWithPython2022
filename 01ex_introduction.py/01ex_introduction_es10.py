# Q9 Normalization 
import numpy as np
a=[2,4,10,6,8,40]

min=np.min(a)
max=np.max(a)

for i, value in enumerate(a):
    a[i]=(value-min)/(max-min)

    
# saving values in tuple
d=tuple(a) 
print("The values after normalization is =",a)
print(d)