#2.List comprehension
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)

print([x**2 for x in range(10) if x%2 == 1])