# 3. Filter list
# Using the filter() hof, define a function that takes a list of words and an integer n as arguments,
#  and returns a list of words that are shorter than n.
list_of_words = ["Ronaldo","Nazo","is","a","God"]
length_of_words = 4
filtered_words = []
def filteri(words,leng):
  shortered_words = []
  # print(words)
  # for i in words:
  # print(len(words))
  if len(words) <= leng:
    # print(len(words))
    shortered_words.append(words)
  return shortered_words

filtered_words = list(filter(lambda words: filteri(words,length_of_words),list_of_words))
print(filtered_words)

# print(filteri(list_of_words,length_of_words))