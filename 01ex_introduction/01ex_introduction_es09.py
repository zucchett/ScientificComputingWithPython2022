nested_list = [(a, b, c) for a in range(0, 100) for b in range(a+1, 100) for c in range(b+1, 100) if a**2 + b**2 == c**2]
print(nested_list)