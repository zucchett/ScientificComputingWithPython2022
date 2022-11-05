#2. List comprehension
import math
# Write the following expression using a list comprehension:

original_list = []
original_list = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(original_list)

new_list = []
new_list = [i*i for i in range(10) if i % 2 == 1]

print(new_list)