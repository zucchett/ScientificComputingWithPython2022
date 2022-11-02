# 1. Global variables

# Convert the function  𝑓  into a function th
# at doesn't use global variables and that does not modify the original list

# -------------------------------------- Code Begin-------------------------------------

x = 5

def f(alist):
    x = 5
    new_list = alist.copy()
    for i in range(x):
        new_list.append(i)
    return new_list

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed

# -------------------------------------- Code End ---------------------------------------

