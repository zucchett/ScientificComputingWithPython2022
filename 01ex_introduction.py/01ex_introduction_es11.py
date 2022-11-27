def PrintFibonacci(length):
    first = 0
    second = 1
    print(first, second, end=" ")

    length -= 2

    while length > 0:

        #Printing the next Fibonacci number.
        print(first + second, end=" ")

        #Updating the first and second variables for finding the next number. 
        t = second
        second = first + second
        first = t

        length -= 1

if __name__ == "__main__":
    print("Fibonacci Series - ")
    PrintFibonacci(20)
    pass