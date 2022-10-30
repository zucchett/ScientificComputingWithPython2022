f1 = 0
f2 = 1
FibonacciList = [0, 1]
for i in range(2, 20):
    fn = FibonacciList[i - 1] + FibonacciList[i - 2]
    FibonacciList.append(fn)

print("The first 20 numbers of the Fibonacci sequence are: ", FibonacciList)