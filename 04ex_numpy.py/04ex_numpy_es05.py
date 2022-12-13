import numpy as np
x = range(1,11) 
n = range(1,11)
multiplication_table = [[i*j for j in x] for i in n]
print(multiplication_table,'\n')
matrix=np.array(multiplication_table)
print(matrix)
# section a
trace_matrix=matrix.trace()
print(trace_matrix)
#section b
def anti_diagonal(matrix):
    return np.fliplr(matrix).diagonal()
print(anti_diagonal(matrix))

# section c
diag=matrix.diagonal(1)   
print(diag)

