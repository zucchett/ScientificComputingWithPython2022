# 2. List Comprehension

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))

andList = [x*x for x in range(10) if x%2 == 1]

print(andList)
