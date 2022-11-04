f=[]

for i in range (20):
    
    f.append(i)
    if i>1:
        f[i]= f[i-1]+f[i-2]
        
print(f)     
        
    
    