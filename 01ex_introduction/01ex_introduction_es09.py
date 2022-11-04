import math

a=0
b=0
c=0

py = [(c,b,a) for c in range(100) for b in range(1,c) for a in range(b) if c*c == b*b+a*a]
print(py)
