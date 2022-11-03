def PrintFibonacci(length):
    first = 0
    second = 1
    print(first, second, end=" ")
    length -= 2
    while length > 0:
        print(first + second, end=" ")
        temp = second
        second = first + second
        first = temp
        length -= 1
if __name__ == "__main__":
    print("Fibonacci Series - ")
    PrintFibonacci(20)