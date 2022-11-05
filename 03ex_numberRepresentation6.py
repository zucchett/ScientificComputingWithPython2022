
def f(n):
  return n*(n-1)

def derivate(f,delta,n):
  return (f(n+delta) - f(n))/delta

for delta in [10**(-2),10**(-4),10**(-6),10**(-8),10**(-10),10**(-12),10**(-14)]:
  print(f"Delta: {delta} , Derivate: {derivate(f,delta,1)}")

