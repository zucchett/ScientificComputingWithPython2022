# Excersize 10:
import math
a = (2,5,8,4)
b=[]
sum,sum2=0,0
for i in a:
    sum += math.pow(i,2)
amp = math.sqrt(sum)
print("V amp:",amp)
for j in a:
    b.append(j/amp)
    sum2 += math.pow(j/amp,2)
print("Vnorm amp:",math.sqrt(sum2))
print("Normalized vector is: ", tuple(b))    
