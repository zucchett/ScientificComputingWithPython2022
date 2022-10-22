# Global variables

def f(n):
    x = n.copy()
    for i in range(5):
        x.append(i)
    return x

alist = [1, 2, 3]
ans = f(alist)
print("Modified list: " + str(ans))
print("Original list: " + str(alist)) # alist has been changed
