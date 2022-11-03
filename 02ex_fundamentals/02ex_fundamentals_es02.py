ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)
ans1=[y**2 for y in range(10) if y%2==1]
print(ans1)
