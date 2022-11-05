import timeit

setup2 = '''
def Fib(i):
    if i<=1:
        return i
    else:
        return Fib(i-2)+Fib(i-1)
'''
code2 = '''
print(list(map(Fib, range(20))))
'''
setup1 = '''
def iterFib(n):
    seq = []
    for i in range(n):
        if (i==0):
            seq.append(0)
        elif (i==1):
            seq.append(1)
        else:
            seq.append(seq[i-1] + seq[i-2])

    print(seq)
'''
code1 = '''
iterFib(20)

'''

print(timeit.timeit(stmt=code1, setup=setup1, number=1))

print(timeit.timeit(stmt=code2, setup=setup2, number=1))

print('The iterative one is faster')