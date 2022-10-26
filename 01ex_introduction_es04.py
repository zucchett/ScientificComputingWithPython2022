count = 0
count1 = 0
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s1l= str.lower(s1)
s2l= str.lower(s2)

print("String 1 is:",s1)
y = input ("enter any letter you want to count in the string above:")
for x in s1l:
    if y==x:
        count= count +1
print(count)

print("String 2 is:",s2)
a = input ("enter any letter you want to count in the string above:")
for i in s2l:
    if a==i:
        count1= count1 +1
print(count1)

    
    


