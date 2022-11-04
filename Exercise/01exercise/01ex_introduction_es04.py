# Excersize 4:
import collections
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
s1=s1.lower()
s2=s2.lower()
results = collections.Counter(s1)
print(results)

#Using dictionary
dictg = {}
for letter in s1:
 if letter not in dictg.keys():
  dictg[letter] = 1
 else:
  dictg[letter] += 1
print(dictg)

d = {}
for i in s1:
    b = s1.count(i,0,len(s1))
    d[i] = b
print(d)