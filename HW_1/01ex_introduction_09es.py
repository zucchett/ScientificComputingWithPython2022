# pythagorean triplets
N = 100
triplet = [(a, b, c) for a in range(1, N//2+1) for b in range(a,N//1+1) for c in range(b,N-1) if a*a + b*b == c*c]
print(str(triplet))
