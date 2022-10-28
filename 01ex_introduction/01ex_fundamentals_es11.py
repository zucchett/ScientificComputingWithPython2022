# 11. The Fibonacci sequence

# Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops.

N = 20
fibonacci = 0

seq = []

for i in range(N+1) :
    if i == 0 or i == 1:
        fibonacci = i
        seq.append(fibonacci)
    else :
        fibonacci = int(seq[i-1]) + int(seq[i-2])
        seq.append(fibonacci)

print("The Fibonacci sequence up to N = 20 is " + str(seq))
