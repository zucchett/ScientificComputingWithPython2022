
words = ["deha","kose","python","calisiyo","a","b","eu","tr","abs","italia"]
n = int(input("Please enter a number:"))
def myFunc(word, n):
    return len(word) < n
print(list(filter(lambda seq: myFunc(seq, n),words)))
