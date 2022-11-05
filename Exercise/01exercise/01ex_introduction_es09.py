# Excersize 9:
import math 
ans=[]
for a in range(1,10):
    for b in range(1,10):
        c2= a**2 + b**2
        c= int(math.sqrt(c2))
        if(c2 == c**2):
            ans.append((a,b,c))
ans = tuple(ans)                     
print(ans)