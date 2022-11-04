# 5. Isolating the unique
# Write a program that determines and counts the unique numbers in the list:
# Do the same exploiting only the Python data structures.只利用Python的数据结构做同样的事情

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
     85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
     1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

l2 = [2, 3, 2, 4, 5, 7]

def uni_num(list):
    newL = []
    for i in list:
        x = list.count(i)
        if x == 1:
            newL.append(i)
    print(newL)


uni_num(l2)





