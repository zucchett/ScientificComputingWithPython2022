# Excersize 11:
a=[]
i=0
while i <20:
    if i <2:
        a.append(i)
    else:
        a.append(a[i-1]+a[i-2])
    i+=1
print(a)
