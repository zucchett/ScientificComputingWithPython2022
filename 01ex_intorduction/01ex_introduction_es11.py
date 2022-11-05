# 11. The Fibonacci sequence

# Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops.

fib = []
for i in range(20): 
    if i==0:
        print('F(0) = 0')
        fib.append(0)
    elif i==1:
        print('F(1) = 1')
        fib.append(1)
    else:
        print('F({}) = {}'.format(i,fib[-1] + fib[-2]))
        fib.append(fib[-1] + fib[-2])
