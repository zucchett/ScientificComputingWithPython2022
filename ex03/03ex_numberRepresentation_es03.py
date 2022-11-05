import math

# underflow
def underflow():
    lower_bound = 1.   
    while lower_bound/2 > 0:
        lower_bound /= 2
    return lower_bound

print("Underflow limit within a factor of 2:", underflow())

# overflow 
def overflow():
    upper_bound = 1.  
    while upper_bound*2. != math.inf:
        upper_bound *= 2.
    return upper_bound

print("Overflow limit within a factor of 2:", overflow())
