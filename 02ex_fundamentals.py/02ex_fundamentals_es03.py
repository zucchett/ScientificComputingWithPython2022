#Filter list

#Using the filter() hof, define a function that takes a list of
# words and an integer n as arguments, and returns a list of words
# that are shorter than n.

test = ["test","meltem","yanoglu","hello","meltemyanoglu","word"]
n = input("Please enter a number for limitation: ")
n = int(n)
def is_shorter(test,n):
    return list(filter(lambda word: len(word) < n, test))

print(str(is_shorter(test, n)))



