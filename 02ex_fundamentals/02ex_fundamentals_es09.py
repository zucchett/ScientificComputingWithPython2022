import timeit

def fibonacci(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

for n in range(20):
    print(fibonacci(n))


def fibonacci_while(n):
    sequence = []
    if n == 1:
        sequence = [0]
    else:
        sequence = [0,1]
        count = 1
        while count + 1 < 20:
            sequence.append(sequence[count-1] + sequence[count])
            count = count + 1
    return sequence

print(fibonacci_while(20))

result = timeit.timeit('fibonacci(n)', globals=globals(), number=20)
result1 = timeit.timeit('fibonacci_while(n)', globals=globals(), number=20)
print("The execution time using the recursive function is ", result)
print("The execution time using while loop is ", result1)