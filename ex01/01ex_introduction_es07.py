import math
numbers_a=[]
for i in range (0,11):
    numbers_a.append(i ** 3)
print(numbers_a)

numbers_b = [i ** 3 for i in range(0,11)]
print(numbers_b)