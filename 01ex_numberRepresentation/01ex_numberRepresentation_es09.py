''' Created by Pedram on 10/22/2022 AD. '''

import math

def pythagoreanTriple():
  for b in range(100):
    for a in range(1, b):
        c = math.sqrt(a**2 + b**2)
        if ((c % 1 == 0) and (a**2 + b**2 < 10000)):
            print("{}\u00b2 +".format(a), "{}\u00b2 =".format(b), "{}\u00b2".format(int(c)), " OR ", "{}\u00b2 +".format(b), "{}\u00b2 =".format(a), "{}\u00b2".format(int(c)))
            
pythagoreanTriple()