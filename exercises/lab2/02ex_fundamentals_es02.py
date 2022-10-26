ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print (ans)

ans1 = [x * x for x in range(10) if x % 2 == 1]
print(ans1)