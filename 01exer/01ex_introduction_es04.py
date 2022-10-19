#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import string
sal = string.ascii_lowercase


s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s1lw = s1.lower()
s2lw = s2.lower()
car1 = len([let1 for let1 in s1lw if let1 in  sal])
car2 = len([let2 for let2 in s2lw if let2 in  sal])



somma1=0
z=0
for i in  s1lw:
    while z < 26:
        #print(i)
        print("Occurence of character",sal[z],"in string s1 =", s1lw.count(sal[z]))
        somma1 += s1lw.count(sal[z])
        i += '1'
        z += 1
print("Number of characters in string1: " + str(car1))
print(somma1)
if somma1 == car1:
    print("Counting of characters in string1 WORKS")
else:
    print("Counting of characters in string1 DOES NOT WORK")
print()
print("Let's focus on the second string")
print()
somma2=0
y = 0
for i in  s2lw:
    while y < 26:
        print("Occurence of character",sal[y],"in string s2 =", s2lw.count(sal[y]))
        somma2 += s2lw.count(sal[y])
        i += '1'
        y += 1
print("Number of characters in string2: " + str(car2))
print(somma2)
if somma2 == car2:
    print("Counting of characters in string2 WORKS")
else:
    print("Counting of characters in string2 DOES NOT WORK")