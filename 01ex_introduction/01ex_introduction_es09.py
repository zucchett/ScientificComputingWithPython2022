pythagoreans  = [(a,b,c) for c in range(1,100) for b in range(1,c) for a in range(1,b) if a*a + b*b == c*c]
pythagoreans = tuple(pythagoreans)
print(pythagoreans)