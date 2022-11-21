def filter_list(L ,n):
    print(list(filter(lambda x: len(x) < n,L)))
test = ["hello","python","scientific","computing","abc"]

filter_list(test,6)    