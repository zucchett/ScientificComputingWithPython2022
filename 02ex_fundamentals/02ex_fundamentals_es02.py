#ex_02 

#Write the following expression using the list comprehension: 
#ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
#print (ans)    

ans = [x * x for x in range (10) if x % 2 == 1]
print (ans)

