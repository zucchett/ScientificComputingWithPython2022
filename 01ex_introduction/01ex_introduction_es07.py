# the code for the the part A of the question : 
list_1 = []
for i in range(0,11) :
    list_1.append(i**3)
print(f'the list with "for" loop is like :  {list_1}')
# the code for the part B of the question : 
list_2 = []
list_2 = [i**3 for i in range(0,11)]
print(f'the list with "list comprehention is like that : {list_2}')
