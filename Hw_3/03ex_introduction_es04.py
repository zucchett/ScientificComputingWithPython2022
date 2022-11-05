a=[]
b=2**-1
c=5
i=0
while True:
    i=i+1
    c=c+b
    b=b*b
    a.append(c)
    print(i,"  ",a[i-1])
    if(b==0):
        break