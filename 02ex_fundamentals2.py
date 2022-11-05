# 2. List comprehension
# Write the following expression using a list comprehension:

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)


#is odd
#Square of the odd list
#Put them on a list!

print(list(i*i for i in range(10) if i % 2 ==1))