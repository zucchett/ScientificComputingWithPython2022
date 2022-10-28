def func(n):
    if n<2:
        return n
    else:
        return func(n-1) + func (n-2)
a =list (map(func,range(20)))
print(a)
