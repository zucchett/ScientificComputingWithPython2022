# 8. The Fibonacci sequence (part 2)

# Calculate the first 20 numbers of the Fibonacci
# sequence using a recursive function.

f = [0, 1, 1]

def fib(n):
    if n==0 or n==1:
        return n
    elif n==2:
        entry = fib(n-1) + fib(n-2)
        return entry
    else:
        entry = fib(n-1) + fib(n-2)
        if entry not in f:
            f.append(entry)
        return entry

N = 20
fib(N)
print(f)

print("Exercise done!")
