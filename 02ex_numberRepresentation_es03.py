def Myfunc(words_list, n):
    return list(filter(lambda word:len(word)<n, words_list))


n = 5
words_list = ['red', 'blue', 'yellow', 'violet', 'green']
print(Myfunc(words_list, n))
