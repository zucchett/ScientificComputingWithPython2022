# # using  a list comprehention 
# num=list(range(11))
# print(num)
# cube_list=[item**3 for item in num]
# print(cube_list) 
    
#using a for loop
num=list(range(11))
print(num)
new_list=[]
for item in num:
    item**=3
    if item not in new_list:
        new_list.append(item)
print(new_list)





