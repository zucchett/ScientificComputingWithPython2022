my_var = 2
add = 1e-1
for i in range (20):
    my_var = my_var + add
    add = add * 1e-1
    print (i)
    print (my_var)
print ("after 14 step , the results are same! ")