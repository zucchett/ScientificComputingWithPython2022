
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s1 = s1.upper()
s2 = s2.upper()

for i in s1:
    a = s1.count(i)
    b = s2.count(i)
    z = a + b
    
    print(i , ": ",z)
 



