txt = input('please insert your sentence : ')
#Write a program that prints the numbers from 1 to 100But for multiples of three print Hello instead of the number and for the multiples of five print World.For numbers which are multiples of both three and five print HelloWorld.

#The quick brown fox jumps over the lazy dog
counter = {}
for i in txt:
    if i.isalpha() == True :
        i = i.upper()
        counter[i] = counter.get(i,0) + 1
print(counter)