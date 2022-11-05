vars = 2
add = 1e-1
for i in range (20):
    vars = vars + add
    add = add * 1e-1
    print (i)
    print (vars)
print ("the results are uniqu untile 14 steps ")