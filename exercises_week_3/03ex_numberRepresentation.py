#3. Underflow and overflow
min = 1
max = 1
N = 150000

for i in range(N): 
    while min/2 != 0:
        min = min/2           
    
while(max*2 != float("inf")):
    max = float(max*2)

print(max)
print(min)
    