a =0
x=0
y=1
l =[]

while a<= 20:
    z = x+y
    x=y
    y=z
    a += 1
    l.append(x)
print(l)
