mylist=[36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
 
list_1 = []
count = {}
for i in mylist:
    count[i] = count.get(i,0) + 1
for i in count:
    if count[i] == 1:
        list_1.append(i)
    
print(f'\nThe unique numbers are: {list_1}')
print(f'\nThere are {len(list_1)} unique numbers in this list.\n')