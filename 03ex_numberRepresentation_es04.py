variable = 2
add = 1e-1
for i in range (20):
    variable = variable + add
    add = add * 1e-1
    print (i)
    print (variable)
print ("after 14 step , the results are same! ")