#ex_10

#Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops.

fibonacci=[0, 1]

f0 = 0
f1 = 1

for i in range(1, 19):
    fibonacci.append(f0+f1)
    f0, f1 = f1, f0+f1

print("The first 20 numbers of the Fibonacci sequence are: \n",fibonacci)
