import timeit

# LOOP FIBONACCI
# timeit loopFibonacci(20)
my_loop_code = """\
def loopfibonacci(n):
    seq = []
    if n == 0:
        seq = [0]
    elif n == 1:
        seq = [0]
    else:
        seq = [0, 1]
        for i in range(1, n - 1):
            seq.append(seq[i - 1] + seq[i])
    return seq
"""
print(timeit.timeit(stmt=my_loop_code))
# RECURSIVE FIBONACCI
# timeit recursiveFibonacci(20)
my_recursive_code = """\
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # uses recursion


def recursivefibonacci(x):
    sequence = []
    for i in range(0, x):
        sequence.append(fibonacci(i))
    return sequence
"""
print(timeit.timeit(stmt=my_recursive_code))
# For loop implementation is faster than recursive implementation
# For loop time = 0.12535809993278235 ;recursive time = 0.32253760006278753
