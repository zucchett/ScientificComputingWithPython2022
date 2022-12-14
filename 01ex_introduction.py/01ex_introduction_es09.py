import math
def pythagorean_triplet(n):  
      for b in range(n):
        for a in range(1, b):
            c = math.sqrt( a * a + b * b)
            if c % 1 == 0:
                print(a, b, int(c))
            
pythagorean_triplet(20)