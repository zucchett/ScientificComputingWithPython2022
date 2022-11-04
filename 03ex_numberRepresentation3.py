import sys

over=0
i=0
while(True):
  try:
    i=2**over
    over=over+0.001
  except OverflowError:
    break
print(f"Overflow value is: {2**(over-0.001)}")

under=0
n=0
while(True):
  try:
    n=1/(2**under)
    under=under+0.001
  except:
    break
print(f"Underflow value is: {1/(2**(under-0.001))}")