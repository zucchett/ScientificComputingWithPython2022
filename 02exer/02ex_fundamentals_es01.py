#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
x = 5
def f(alist = None):
    if alist == None:
        alist = [1,2,3]
        for i in range(x):
            alist.append(i)        
    return alist

alist = [1, 2, 3]
ans = f(alist)
print("ANS = ",f())
print("ALIST = ",alist)