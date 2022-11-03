s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s1 = s1.lower()
print(s1)
for i1, c1 in enumerate(s1):
    if (c1 not in s1[:i1]):
        print(c1,":",s1.count(c1))
        
s2 = s2.lower()
print(s2)
for i2, c2 in enumerate(s2):
    if (c2 not in s2[:i2]):
        print(c2,":",s2.count(c2))