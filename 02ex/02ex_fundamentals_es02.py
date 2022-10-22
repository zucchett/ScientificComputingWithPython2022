# List comprehension

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print("Original output: " + str(ans))

ant = [x*x for x in range(10) if x % 2 == 1]
print("List comprehension output: " + str(ant))
