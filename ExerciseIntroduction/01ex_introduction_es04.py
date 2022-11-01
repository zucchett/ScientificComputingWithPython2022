"""
4. Counting letters
Write a program that calculates the number of times each character occurs in a given string. Ignore differences in
capitalization.
The strings are in the cell below.
"""

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

list_s1 = list(s1.lower())
list_s2 = list(s2.lower())
list_s3 = list_s1

counter1 = {i: list_s1.count(i) for i in list_s1}
counter2 = {i: list_s2.count(i) for i in list_s2}

for i in range(len(list_s2)):
    list_s3.append(list_s2[i])

counter3 = {i: list_s3.count(i) for i in list_s3}

print("The number of each character in the first string: \n", counter1)
print()
print("The number of each character in the second string: \n", counter2)
print()
print("The number of each character in total: \n", counter3)
print()
