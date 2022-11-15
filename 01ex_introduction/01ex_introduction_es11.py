# 11. The Fibonacci sequence
# Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops.

# finona = []
# while 2 < len(finona) < 20:
#     x = finona[-1]+finona[-2]
#     finona.append(x)
#
# print(finona)


def fib2(n=20):
    i = 0
    a, b = 0, 1
    finona = []
    while i < n:
        i += 1
        finona.append(b)
        a, b = b, a + b
    return finona


print(fib2(20))

# for
# a = 0
# b = 1
# finona = []
#
# for i in range(20):
#     a, b = b, a + b
#     finona.append(a)
# print(finona)
