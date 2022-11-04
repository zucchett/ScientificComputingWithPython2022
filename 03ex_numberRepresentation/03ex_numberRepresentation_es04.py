n = 3.6
smaller = 0.001
check = True    #for accuracy

while check:
    if n + smaller == n:
        check = False
    else:
        smaller = smaller/10

print('The machine precision is : ', smaller)
