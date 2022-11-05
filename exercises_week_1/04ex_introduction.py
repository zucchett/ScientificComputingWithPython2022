#4. Counting letters

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
s3 = "The pool is thin"

dict = {}
#you can change the string here
string = s2.lower()

for i in range(0,len(string)):
    char = string[i] #write the sentence in lower case and select each character
    char_count = string.count(char) #count how many times the character is repeated
    dict[char] = char_count #insert the character and its count in the dictionary(so there are no repetitions)
print(dict)