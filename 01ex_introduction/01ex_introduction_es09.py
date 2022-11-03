#9.Nested list comprehensions

def EqInteger(x):
  """EqInteger defines whether a float is equivalent to an integer"""
  y=int(x)
  if x-y == 0:
    return True
  else:
    return False
  
#main
from math import sqrt
a=3
b=4
c=5
T=()
while c<100:
  while c<100:
    if EqInteger(c):
      T=T+((a,b,int(c)),)
    b=b+1
    c=sqrt(a**2+b**2)
  b=4
  a=a+1
  c=sqrt(a**2+b**2)
print("Unique Pythagorean triples for the positive integers a,b and c having c < 100:\n",T)
