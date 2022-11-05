import  collections


s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def calculator(sentence):
    counter = collections.defaultdict(int)
    for word in sentence:
        counter[word] += 1
    return counter

for x in [s1,s2]:
    print(f"The number of each characters in the sentence:\n {x}\n {calculator(x)} \n")