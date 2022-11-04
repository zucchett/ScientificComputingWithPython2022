import math as m
n = int(input("Enter the dimention"))

Vector = []
Vector_length_2 = 0
Vector_length_tmp = 0
for i in range(n):
    x = int( input(f"Enter the {i+1} element  V[{i}]:"))
    Vector.append(x)
    Vector_length_tmp += x**2
    
Vector_length = m.sqrt((Vector_length_tmp))
Normalize_vector =  [element/Vector_length for element in Vector]
print('Normalize_vector : ', Normalize_vector)