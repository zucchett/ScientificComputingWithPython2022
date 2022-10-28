#Zuccolo Giada, matr. 2055702
#EXE 3

n = int(input("enter n = "))
bow = [
    "apple", "music", "guitar", "pie", "computer", "piano", "sing", "turing", "python"
]


def check(bow, n):
    def short(bow):
        if len(bow) < n:
            return bow

    bow = list(filter(short, bow))
    return bow


print(check(bow, n))