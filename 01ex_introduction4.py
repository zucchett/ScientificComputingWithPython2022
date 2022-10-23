s1= "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def countchar(s):
    s=s.lower()
    count_char= {}
    for character in s:
        if character in count_char:
            count_char[character] += 1
        else:
            count_char[character] = 1
    print("The count of characters in the string is:")
    print(count_char)

countchar(s1)
print("_______________________________________________________________________________________")
countchar(s2)
print("_______________________________________________________________________________________")
countchar(s1+s2)
