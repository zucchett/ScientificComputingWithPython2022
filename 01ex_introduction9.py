print([(a, b, c) for a in range(1, 100 ) for b in range(a,100 )
       for c in range(b, 100) if a**2 + b**2 == c**2])

