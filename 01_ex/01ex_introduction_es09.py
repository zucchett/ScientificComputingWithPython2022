A=list([(a, b, c) for c in range(0,100) for b in range(1, c) for a in range(b) if c * c == a * a + b * b])
print(tuple(A))