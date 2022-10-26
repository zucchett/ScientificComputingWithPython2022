def loopFibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(1, n+1):
            if(i == 0):
                fibonacci_list.append(a)
            elif(i == 1):
                fibonacci_list.append(b)
            else:
                c = a + b
                a = b
                b = c
                fibonacci_list.append(c)

fibonacci_list=[]
loopFibonacci(20)
print(fibonacci_list)