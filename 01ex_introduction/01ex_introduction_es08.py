import itertools
result_list = [(i,j) for i,j in itertools.product([0,1,2],[0,1,2,3])]
print(result_list)
