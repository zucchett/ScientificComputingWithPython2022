# Counting letters

input_string = input("Enter the string: ")
lower_input_string = input_string.lower()

result = {}

for i in input_string:
    if i not in result:
        result[i] = 1
    else:
        result[i] = result[i] + 1

print(result)
