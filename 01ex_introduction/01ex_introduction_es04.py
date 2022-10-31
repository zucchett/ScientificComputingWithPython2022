
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


s1 = s1.lower()
s2 = s2.lower() 

char_in_s1 = {}
for i in s1:
    if i in char_in_s1:
        char_in_s1[i] = char_in_s1[i] +1
    else:
        char_in_s1[i] = 1


char_in_s2 = {}
for i in s2:
    if i in char_in_s2:
        char_in_s2[i] = char_in_s2[i] +1
    else:
        char_in_s2[i] = 1

print(char_in_s1)
print(char_in_s2)
