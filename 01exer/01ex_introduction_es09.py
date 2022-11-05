#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
l = []

for c in range(1,100):
    for b in range(1,100):
        for a in range(1,100):
            if a**2 + b**2 == c**2 and a < b and b < c:
                l.append((a,b,c))



l = tuple(l)
print(l)












