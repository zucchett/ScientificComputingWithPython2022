n = 100
                
Pythagorean = [ (a,b,c) for a in range(1,n+1) for b in range(a,n+1) for c in range(b,n+1) if a*a + b*b == c*c ]
print(Pythagorean)
