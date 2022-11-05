s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


# A character can be an alphabet or numbern or all the punctuations 
def count_character(s):
    count = dict()
    for char in set(s):   
        count[char] = s.lower().count(char)
    return count

print('count of the character of string S1 is {} \n \n'.format(count_character(s1)))
print('count of the character of string S2 is {}'.format(count_character(s2)))
