a=[]
b=[]
c=1
d=1
i=0

while True:
    i=i+1
    c=c*2
    d=d/2
    try:
        a.append("%.5e"%c)
    except:
        print(i)
        print("Counter:" ,i-1, "and overflow number:",a[i-2])
        break

j=0
while True:
    j=j+1
    d=d/2
    b.append(d)
    if (b[j-1]==0):
        print("Counter:" ,i+j-1, "and underflow number:",b[j-2])
        break
