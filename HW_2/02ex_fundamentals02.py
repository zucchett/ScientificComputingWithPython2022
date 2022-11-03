# list comprehension
# without list comprehension { ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))) }

new_ans = [i * i for i in range(10) if i % 2 == 1]
print(new_ans)
