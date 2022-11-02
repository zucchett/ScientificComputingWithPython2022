# Underflow and overflow

from math import inf

overflow = 1
underflow = 1

while(overflow*2 > overflow and float(overflow*2) != inf):
	overflow= float(overflow*2)

while(underflow/2<underflow and float(underflow/2) != 0.0):
	underflow= float(underflow/2)

print(overflow)
print(underflow)