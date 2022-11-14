def fibonacci(num):
    listOfFibonacci = []
    for num in range(num):
        if num <= 1 :
            listOfFibonacci.append(num)
        else:
            listOfFibonacci.append(listOfFibonacci[num-1] + listOfFibonacci[num-2])
    return listOfFibonacci
fibonacci(20)
def fibonacci(num):
    if num <= 1 :
        return num
    else:
        s = fibonacci(num-1) + fibonacci(num-2)
        return s
num = 20
print("Fibonacci sequence:")
for i in range(num):
    print(fibonacci(i))