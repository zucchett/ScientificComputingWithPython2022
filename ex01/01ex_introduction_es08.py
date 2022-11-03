from itertools import product
list = [(x,y) for x,y in product([0,1,2],[0,1,2,3])]
print(list)
