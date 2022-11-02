#3. Underflow and overflow
import sys
min = 1
max = 1
N = 150000

for i in range(N): 
    while min/2 != 0:
        min = min/2           
    max = max*2

print(max)
print(min)
    