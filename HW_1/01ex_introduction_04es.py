s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
s1_new = s1.lower()  # converting everSything to lowercase to make sure
s2_new = s2.lower()  # each character is counted only once

count1 = {}  # this creates an empty dictionary
count2 = {}  # this creates an empty dictionary

for i in s1_new:  # 'i' is first 'w',next 'r', 'i' and so on
    if i in count1:  # checks if 'i' was previously in the dictionary before
        count1[i] += 1  # if the character is already present count is incremented by 1
    else:
        count1[i] = 1  # if the character is not present count is just 1

for j in s2_new:  # 'j' is first 'w',next 'r', 'i' and so on
    if j in count2:  # checks if 'j' was previously in the dictionary before
        count2[j] += 1  # if the character is already present count is incremented by 1
    else:
        count2[j] = 1  # if the character is not present count is just 1
print("count of the characters in string s1"+str(count1))  # converting dictionary to string to display
print("count of the characters in string s2"+str(count2))  # converting dictionary to string to display
