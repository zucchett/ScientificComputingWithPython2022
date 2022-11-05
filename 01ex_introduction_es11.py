# EXCERSICE 11

print ("-------------Excersice 8: Fibonacci Sequence-----------------")


n1, n2 = 0, 1
count = 0

print("Fibonacci sequence:")

for nterms in range (20):
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

