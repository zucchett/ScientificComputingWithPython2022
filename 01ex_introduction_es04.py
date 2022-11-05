s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

# print('a: ', s1.count('a') + s1.count('A') + s2.count('a') + s2.count('A')  )

for i in range(65 , 97):
    print(chr(i),': ', s1.count(chr(i)) + s1.count(chr(i + 32)) + s2.count(chr(i)) + s2.count(chr(i +32))  )

