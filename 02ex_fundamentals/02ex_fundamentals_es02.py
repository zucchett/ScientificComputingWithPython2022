ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))

my_ans = [i*i for i in range(10) if i % 2 ==1]

print("Result of the original list definition: \n", ans)
print()
print("Result using list comprehension: \n", my_ans)
