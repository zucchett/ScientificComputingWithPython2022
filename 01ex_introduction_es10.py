numbers = []

while True:
    a = int(input("enter number---for stop enter '0':  "))
    if a == 0:
        break
    else:
        numbers.append(a)

s = sum(numbers)

norm = []
for i in numbers:
    norm.append(i/s)

print("norm: ", norm)

q = sum(norm)
print("sum of norm: ",q)
