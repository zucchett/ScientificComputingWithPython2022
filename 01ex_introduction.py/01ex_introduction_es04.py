#Letter Counting

input = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
test_new = input.lower()

result = {}

for i in test_new:
    if i not in result:
        result[i] = 1
    else:
        result[i] = result[i] + 1

print("Count of the characters in test string: ",result)