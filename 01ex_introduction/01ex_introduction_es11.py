f_list = []
for i in range(4):
    if (len(f_list) < 2):
        f_list.append(i)
    else:
        f_list.append(f_list[i-1] + f_list[i-2])
print(f_list)