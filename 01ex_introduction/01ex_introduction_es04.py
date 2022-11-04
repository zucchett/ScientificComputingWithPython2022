from collections import Counter

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s=s1+s2

def cali_str(s):
    count = Counter(s.lower())
    for i in range(97, 123): #ascii alphabet numbers from a to z
        print(chr(i), ":", count[chr(i)])
    print("space:", count[" "])
    
cali_str(s)

    
