x = 5

def f(alist):
	y=alist[:]
	for j in range(x):
        	y.append(j)
	return y

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed
