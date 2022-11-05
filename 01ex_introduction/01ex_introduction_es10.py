from math import sqrt
# we insert a vector in list for example :
vector,sum= [1,4,6,7,5,6],0
for  i in vector :
    sum  = sum + (i**2)
total = sqrt(sum)
normal_vector = [i/total for i in vector]
print(normal_vector)