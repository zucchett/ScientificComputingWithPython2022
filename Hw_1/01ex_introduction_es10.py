import math

vec=[9,39,34,35,45]

def len_vec(list):
    lenght_of_vector=0
    for i in range(len(list)):
        lenght_of_vector=vec[i]*vec[i]+lenght_of_vector  
    return math.sqrt(lenght_of_vector)

def normalization(list):
    sqroot=len_vec(list)
    norm_ratio=1/sqroot
    lenght=[]
    for i in range(len(list)):
        lenght.append(list[i]*norm_ratio)
    return lenght


lenght=normalization(vec)
sum=0
for i in range(0, len(vec)):
    sum=lenght[i]**2+sum
print("Normalization: ",lenght)
print("Sum of all the entries is ",sum)
