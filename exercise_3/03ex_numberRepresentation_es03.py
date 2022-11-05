from ast import Try
from cmath import inf
from typing import overload


def determineOverUnderFlow():
    a = 1.0
    b = 1.0
    overflowcounter, underflowcounter = 0,0


    while(a != inf):
        a = a + 2
        overflowcounter += 1
        #print(a)

    print("Over Flow Counter: ", overflowcounter)

    while(b != 0.0):
        b = b/2.0
        underflowcounter += 1
        #print(b)
    print("Under Flow Counter: ", underflowcounter)

determineOverUnderFlow()        