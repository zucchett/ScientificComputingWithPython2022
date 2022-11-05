# a) 
cube_list_a = []
for x in range(11):
    x = x ** 3
    cube_list_a.append(x)
print("For Loop:", cube_list_a)

# b)
cube_list_b = [x * x * x for x in range(11)]
print("List Comprehension:", cube_list_a)