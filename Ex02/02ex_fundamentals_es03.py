#3. Filter List

def filterWords(words,number):
    return list(filter(lambda x: len(x) < number, words))


a = filterWords(['fat', 'cat', 'erei', 'qwerty','postit'],4)

print(a)