#5. Isolationg the unique

#inputs
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

l1 = [3,4,6,6,4]

#outputs
total_unique = 0;
unique=[]

#chose a list
list = l

for i in range(0,len(list)):
    num = list[i]   
    if list.count(num)==1:
        unique.append(num)
        total_unique += 1
print(f"These are the unique numbers: {unique}")
print(f"The total number of unique numbers is: {total_unique}")
