# Normalization of a N-dimensional vector

import math

def normalize(tuple_v): 
    counter = 0 
    list_tuple = list(tuple_v)
    squared_sum = 0 
    for i in list_tuple:      
        squared_sum += int(i)**2
    sqrt_squared_sum = math.sqrt(squared_sum)
    for j in list_tuple:
        j = int(j) / sqrt_squared_sum
        list_tuple[counter] = j
        counter = counter + 1
    return tuple(list_tuple)
    
vector = input("Input tuples by separating comma (,): ")
new_vector = []
list_vector_str = vector.split(",")
print(list_vector_str)
if len(list_vector_str) >= 2:
    for i in range(0, len(list_vector_str)):
        new_list = list_vector_str[i].replace(' ', '') 
        tuple_v = tuple(new_list)
        new_vector.append(tuple_v)

new_vector_normalized = []
for i in new_vector:
    new_vector_normalized.append(normalize(i))

print(new_vector_normalized)

        


