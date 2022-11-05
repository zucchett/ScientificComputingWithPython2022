def Myfunc(words_list, n):
    return list(filter(lambda word:len(word)<n, words_list))


n = 5
words_list = ['red', 'blue', 'yellow', 'violet', 'green']
print('list :', words_list)
print('list of words that are shorter than n=5', Myfunc(words_list, n))
