'''
print("ex. 1")
2, 5, 6
'''



print("ex. 2")

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))

print(ans)

# Rewrited expression using a list comprehension

ans = [ x**2 for x in range(10) if (x**2 % 2 == 1) ] 

print(ans)

