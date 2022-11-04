# for loop
x=[]
for i in range(11):
    x.append( pow(i, 3))
print('result by for loop', x)    
# list comprehension
x = [pow(i,3) for i in range(11)]
print('result by list comprehension', x)    

