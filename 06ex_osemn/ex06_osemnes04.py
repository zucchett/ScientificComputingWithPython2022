from itertools import islice
with open ('../data/credit_card.dat', mode = 'r') as file:
    data = file.readlines()
creditcards = open('../data/credit_cards.txt', 'a+')
def get_char(n, d):
    return chr(int(d[6*n:6*(n+1)], 2))
for d in data:
    if len(d) == 119:
        a = []
        n = 0
        for x in range(19):
            a.append(get_char(n, d))
            n += 1
        a.append('\n')
        creditcards.write("".join(a))
        print("".join(a))

