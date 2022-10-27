numbers = []

while True:
    a = int(input("enter number---for stop enter '0':  "))
    if a == 0:
        break
    else:
        numbers.append(a)

b = []
for i in numbers:
    b.append(i**2)

s = sum(b)

norm = []
for i in b:
    norm.append(i/s)

print("norm: ", norm)

q = sum(norm)
print("sum of norm: ",q)