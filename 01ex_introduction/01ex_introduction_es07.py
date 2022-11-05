
out1 = []

for i in range(11):
    out1.append(pow(i,3))

print(out1)


out2 = [pow(x,3) for x in range(11)]
print(out2)