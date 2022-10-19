# 11. The Fibonacci sequence
# Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops.
print("The first 20 numbers of the Fibonacci sequence!")
fib_seq = [0,1]
[fib_seq.insert(i+2,fib_seq[i+1] + fib_seq[i]) for i in range(18)]
print(fib_seq)
