s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."

s2 = "The quick brown fox jumps over the lazy dog"

def counting_letters(string):
    #create dictionary to hold results
    count = {}
    for char in string.lower():
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    #print the results
    for key in count:
        if count[key] > 1:
            print(key, count[key])


counting_letters(s1)