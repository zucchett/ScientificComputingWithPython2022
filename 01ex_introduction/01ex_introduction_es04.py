def count_letters(myString):
    l = []
    for i in range(len(myString)):
        l.append(myString[i])
    characters,iterations = [],[]
    a = dict
    for x in l:
        if x not in characters:
            characters.append(x)
            iterations.append(l.count(x))
    zipped = zip(characters,iterations)
    print(list(zipped))
    
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog" 

count_letters(s1.lower())
print("----------------------\n")
count_letters(s2.lower())
