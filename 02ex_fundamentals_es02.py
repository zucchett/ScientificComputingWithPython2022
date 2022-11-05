# ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))

li= [1,2,3,4,5,6,7,8,9,10]
a = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1,li)))

print(a)
