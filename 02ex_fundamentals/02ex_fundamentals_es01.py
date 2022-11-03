x = 5

def f(local_list, x):
	x_local = x
	for i in range(x_local):
		alist.append(i)
	return local_list

alist = [1, 2, 3]
ans = f(alist.copy(), x)
print(ans)
print(alist) # alist has been changed
