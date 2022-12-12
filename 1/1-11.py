
def Fibonacci(length):
    a = 0
    b = 1
    length -= 2
    x = [0,1]
    while length > 0:

        temp = b
        b += a
        x.append(b)
        a = temp

        length -= 1
    return(x)

Fibonacci(20)