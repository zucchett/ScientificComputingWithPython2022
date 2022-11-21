from math import sqrt
l = [12, 15, 4, 18, 450, 603, 179, 1500] #list to be normalized
L = [i**2 for i in l]
Norm = sqrt(sum(L))
for i in range(len(l)):
    l[i]/=Norm
l_squared = [i**2 for i in l]
print('Normalized list:\n',l,'\n\nsum of the list squared:',sum(l_squared))