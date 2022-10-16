# count the unique numbers in the list
num_list = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18,
            63, 70, 85, 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56,
            51, 79, 81, 57, 37, 91, 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50,
            95, 90, 98, 39, 16, 82, 31, 92, 41, 45, 30, 66, 70, 34, 85, 94, 5,
            3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
count = 0  # count the number of unique numbers
unique = []  # initializing an empty list
for i in num_list:
    if i not in unique:  # checks if the number was previously in the unique list before
        count += 1  # increments everytime we find a unique number
        unique.append(i)
print(str(count) + " unique numbers in the list are" + str(unique))  # converting dictionary to string to display

# count the numbers that exist in the list only once
num_list = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18,
            63, 70, 85, 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56,
            51, 79, 81, 57, 37, 91, 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50,
            95, 90, 98, 39, 16, 82, 31, 92, 41, 45, 30, 66, 70, 34, 85, 94, 5,
            3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

count = 0  # count the number of unique numbers
unique = []  # initializing an empty list
for i in num_list:
    n = num_list.count(i)  # count the no. of times 'i' is present in the list
    if n == 1:  # checks if the number is present in the list more than once
        count += 1  # increments everytime we find a unique number
        unique.append(i)  # adds the unique number to the list

print(str(count) + " unique numbers in the list are" + str(unique))  # converting dictionary to string to display
