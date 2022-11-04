# 3. Underflow and Overflow
import math


underflow = 1.0
overflow = 1.0 # Because if we use integer 1, python has unlimited precision for integers

underflowLimit = 0
while underflow > 0:
    try:
        underflow = underflow/2
        underflowLimit+=1
    except:
        break

overflowLimit = 0
while overflow != math.inf:
    try:
        overflow = overflow * 2
        overflowLimit+=1
        print(overflow)
    except:
        break


print("\nUnderflow occurs at: 2^(-%d)" % underflowLimit)
print("\nOverflow occurs at: 2^%d" % overflowLimit)
