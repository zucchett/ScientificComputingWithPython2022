#Unique Numbers

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18,
            63, 70, 85, 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56,
            51, 79, 81, 57, 37, 91, 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50,
            95, 90, 98, 39, 16, 82, 31, 92, 41, 45, 30, 66, 70, 34, 85, 94, 5,
            3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
count = 0  #unique numbers counter
unique_num = []
for i in l:
    if i not in unique_num:
        count += 1
        unique_num.append(i)
print(str(count) + " unique numbers are: \n" + str(unique_num))
