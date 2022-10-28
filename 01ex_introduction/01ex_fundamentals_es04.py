# 4. Counting letters

# Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."

s2 = "The quick brown fox jumps over the lazy dog"

s11 = s1.lower()
s22 = s2.lower()

dicts = {} # dictionary for string s1
for char in s11:
    if char in dicts :
        dicts[char] += 1
    else :
        dicts[char] = 1

print("String s1: " + str(dicts))
for key, value in dicts.items():
    if value == 1 :
        print("Letter " + key + " occurs once.")
    elif value == 2 :
        print("Letter " + key + " occurs twice.")
    else :
        print("Letter " + key + " occurs " + str(value) +  " times.")

dicts2 = {} # dictionary for string s2
for char2 in s22:
    if char2 in dicts2 :
        dicts2[char2] += 1
    else :
        dicts2[char2] = 1

print("String s2: " + str(dicts2))
for key, value in dicts2.items():
    if value == 1 :
        print("Letter " + key + " occurs once.")
    elif value == 2 :
        print("Letter " + key + " occurs twice.")
    else :
        print("Letter " + key + " occurs " + str(value) +  " times.")
