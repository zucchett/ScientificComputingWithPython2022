print(tuple([(a, b, c) for c in range(100) for b in range(1, c) for a in range(b) if c * c == a * a + b * b]))
