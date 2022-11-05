# Write a function that takes the above dictionary and uses the map()
# higher order function to return a list that contains the length of the keys of the dictionary.
lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}
list_keys = list(lang.keys())
print(list_keys)


def find_length(k):
    print("The key is:", k)
    return len(k)


for j in map(find_length, list_keys):
    print(j)
