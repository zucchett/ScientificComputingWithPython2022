import numpy as np
M_1= range(1,11) 
M_2= range(1,11)

mult_table = [[i*j for j in M_1] for i in M_2]
mult_table = np.array(mult_table) # convert list to numpy array
print(mult_table) 

print("\nTrace of matrix:",np.trace(mult_table))

def anti_diagonal(arr):
    return np.fliplr(arr).diagonal()
print("Anti-diagonal matrix:",anti_diagonal(mult_table))

print("Diagonal offset by 1 upwards:",np.diagonal(mult_table,1))