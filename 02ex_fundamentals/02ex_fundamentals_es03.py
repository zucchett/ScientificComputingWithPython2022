# 3. Filter list

# Using the filter() hof, define a function
#  that takes a list of words and an integer n as arguments,
#  and returns a list of words that are shorter than n.
# DONE

def wrapper(words, n):

    def is_shorter(w):
        if len(w)<n:
            return True
        return False

    output = list(filter(is_shorter, words))

    return output

word_list = ["Hi", "this", "program", "is", "really", "cool"]
word_length = int(input("The words in the list should be shorter than: "))

filtered_list = wrapper(word_list, word_length)

print("The list of words is: ", *word_list)
print("After filtering, the new list is:", *filtered_list)
