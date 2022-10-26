
def filter_words(words,n):
    return list(filter(lambda x: len(x) < n, words))


words = ['salim','benhamadi','university','of','padova','yes','no']
n = 4

print('the words that are shorter than {} are {}'.format(n, filter_words(words,n)))
