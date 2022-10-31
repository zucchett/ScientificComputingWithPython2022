
seq = []
for i in range(20):
    if (i==0):
        seq.append(0)
    elif (i==1):
        seq.append(1)
    else:
        seq.append(seq[i-1] + seq[i-2])

print(seq)