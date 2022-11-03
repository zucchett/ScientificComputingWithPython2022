#2. List comprehension

#Initial code
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)

#Modified code
ans=[x**2 for x in range(10) if x % 2 == 1]
print(ans)
