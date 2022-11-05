# using for loop

def loopFibonacci(n):
    seq = []
    if n == 0:
        seq = [0]
    elif n == 1:
        seq = [0]
    else:
        seq = [0,1]
        for i in range(1, n-1):
            seq.append(seq[i-1] + seq[i])
    return seq


print(loopFibonacci(20))
