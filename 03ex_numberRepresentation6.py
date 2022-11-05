# 6. The derivative


# Write a program that implements the function  𝑓(𝑥)=𝑥(𝑥−1)
# d𝑓d𝑥=lim𝛿→0𝑓(𝑥+𝛿)−𝑓(𝑥)𝛿

def f(x):
  return x*(x-1)

def derivate(f,delta,x):
  return (f(x+delta) - f(x))/delta

for delta in [10**(-2),10**(-4),10**(-6),10**(-8),10**(-10),10**(-12),10**(-14)]:
  print(f"Delta: {delta} , Derivate: {derivate(f,delta,1)}")

