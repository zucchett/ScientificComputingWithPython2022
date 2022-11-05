''' Created by Pedram on 10/26/2022 AD. '''

def checkCount(x):
    return len(x) < number

text = input("Please input a list of words to evaluate: ")
number = int(input("Please input a number: "))
wordsList = []
for words in text.split():
    wordsList.append(words)
print(list(filter(checkCount, wordsList)))