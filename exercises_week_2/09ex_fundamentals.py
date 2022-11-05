#9. The Fibonacci sequence (part 3)
import timeit

def recursiveFibonacci(n):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return(fibonacci(n-1) + fibonacci(n-2))

    f_sequence =[]
    for i in (range(5)):
        f_sequence.append(fibonacci(i))
    return(f_sequence)

def loopFibonacci(n):
    sequence = []   

    sequence.insert(0,0)
    sequence.insert(1,1)

    for i in range(2,n):
        sequence.append(sequence[i-1]+sequence[i-2])
    return f"The first 20 numbers of the Fibonacci sequence are: {sequence}"

print(timeit.timeit("loopFibonacci(20)",globals=globals()))
print(timeit.timeit("recursiveFibonacci(20)",globals=globals()))

#from this analysis the loopFibonacci appears faster by 3s