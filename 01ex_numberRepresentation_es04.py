s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s1 = s1.lower()
print(s1)

import string

chars = list(string.printable)

count = []

for character in chars:
    count = s1.count(character)
    print(count,character)
