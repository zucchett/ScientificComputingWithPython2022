#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
#print(a)

d = [(x, y) for x in range(3) for y in range(4)]
#print(d)

if a == d:
    print("The two methods are equivalent")
else:
    print("The prgram DOES NOT WORK")