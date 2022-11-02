
l = [4,2,8]
b=[]
for i in l:
    s= i**2
    b.append(s)
v = sum(b)
a = []
for i in b:
    a.append(i/v)

print(a)
print(sum(a))


