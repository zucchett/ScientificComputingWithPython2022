s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s1 = s1.lower()
s2 = s2.lower()

character_count_s1 = {}
character_count_s2 = {}

print("Counting letters s1: ")
for i in s1:
    if not i in character_count_s1:
        character_count_s1[i] = s1.count(i)

print(character_count_s1)

print("Counting letters s2: ")
for i in s2:
    if not i in character_count_s2:
        character_count_s2[i] = s2.count(i)

print(character_count_s2)