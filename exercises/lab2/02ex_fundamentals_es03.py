# Filter list

list_words = ["The", "quick","brown", "fox", "jumps", "over", "the", "lazy", "dog"]
n = 5
print(list(filter(lambda x: len(x)<n,list_words)))