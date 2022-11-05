s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

charsList = {}
for char in s1:
    chrLower = char.lower()
    if chrLower in charsList:
        charsList[chrLower] += 1
    else:
        charsList[chrLower] = 1
print(charsList)

charsListS2 = {}
for char in s2:
    chrLower = char.lower()
    if chrLower in charsListS2:
        charsListS2[chrLower] += 1
    else:
        charsListS2[chrLower] = 1
print(charsListS2)
