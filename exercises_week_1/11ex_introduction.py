#11. Fibonacci sequence

sequence = []   

sequence.insert(0,0)
sequence.insert(1,1)

for i in range(2,20):
    sequence.append(sequence[i-1]+sequence[i-2])
print(f"The first 20 numbers of the Fibonacci sequence are: {sequence}")
