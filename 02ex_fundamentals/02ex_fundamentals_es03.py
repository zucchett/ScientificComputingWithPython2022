def word_lenght(x, n):
    return len(x) > n

words = [item for item in input("Input the words you want separated by a space : ").split(" ")]
m = int(input("Enter an integer number: "))
print()

words_reduced = list(filter(lambda elements : word_lenght(elements, m), words))

print("The filtered list of words is: \n", words_reduced)
