from collections import Counter
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
s1Count=Counter(s1)
s2Count=Counter(s2)
print("string 1 characters and occurences  ",s1Count)
print("string 2 characters and occurences  ",s2Count)