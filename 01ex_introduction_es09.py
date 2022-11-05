import math
def pyth(n):
  for b in range(n):
    for a in range(1, b):
        c = math.sqrt( a * a + b * b)
        if c % 1 == 0:
            print("the answer is: ",a, b, int(c))
            
pyth(int(input("enter the number: ")))




