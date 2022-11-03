def enum(a):
        n=6
        return len(a)<n

words=["banana", "ananas","mela", "uva", "pera"]
y=list(filter(enum,words))
print(y)

