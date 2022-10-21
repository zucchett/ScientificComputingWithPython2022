f1 = 0
f2 = 1
fiboList = [0, 1]
for x in range(2, 20):
    fn = fiboList[x - 1] + fiboList[x - 2]
    fiboList.append(fn)

print("The first 20 numbers of the Fibonacci sequence are: ", fiboList)
