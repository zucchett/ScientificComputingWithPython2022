#ex_09 
#Find and put in a tuple all unique Pythagorean triples for the positive integers 𝑎, 𝑏 and 𝑐 with 𝑐<100.

pytagorean = tuple([(a, b, c) for a in range(1,100) for b in range(1,100) for c in range(1,100) if a**2. + b**2. == c**2. if a < b if b < c])

print(pytagorean)     
