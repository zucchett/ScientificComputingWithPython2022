# Counting letters

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."

s2 = "The quick brown fox jumps over the lazy dog"

s1 = s1.lower() #ignoring cases
s2 = s2.lower() #ignoring cases

print(s1,s2)

charCountDict = {}

for char in s1:
    if char not in charCountDict:
        charCountDict[char] = 1
    else:
        charCountDict[char] += 1

print(charCountDict)

