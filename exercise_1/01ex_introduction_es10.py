import math
normal_vec = []
example_list = [4,5,6]
n = 0
for i in example_list:
    n = n + i*i
    newlist = math.sqrt(n)
print(i)

for j in example_list:
    normal_vec.append(j/newlist)
print(normal_vec)