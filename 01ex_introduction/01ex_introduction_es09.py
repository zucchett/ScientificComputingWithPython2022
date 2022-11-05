print([(a,b,c) for c in range(100,1,-1) for b in range (100,1,-1) for a in range(100,1,-1) if c**2 == (b**2)+(a**2)])
