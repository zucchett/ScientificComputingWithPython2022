
# 3. Filter list

# Using the filter() hof, define a function that takes a list of
# words and an integer n as arguments,
# and returns a list of words that are shorter than n.


# -------------------------------------- Code Begin-------------------------------------

def filter_words(words,n):
    return list(filter(lambda x: len(x) < n, words))


words = ['salim','benhamadi','university','of','padova','yes','no']
n = 4

print('the words that are shorter than {} are {}'.format(n, filter_words(words,n)))

# -------------------------------------- Code End ---------------------------------------
