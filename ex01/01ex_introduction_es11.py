def Fib(length):
    first = 0
    second = 1
    print(first, second)
    length -= 2
    while length > 0:
        print(first + second)
        temp = second
        second = first + second
        first = temp
        length -= 1

Fib(20)