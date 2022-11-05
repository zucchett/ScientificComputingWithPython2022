#ex_05
#Write a program that determines and counts the unique numbers in the list:

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

#len(l) was 80.

setl = set(l) #plugging the list in the set in order to eliminate duplicates

values = len(setl) #counts unique numbers = lenght of the set 
print("There are", values, "unique numbers in the list and they are:")  

listl = (list(setl)) #reconvert the set in the list

for item in listl:
    print(item)


#Do the same exploiting only the Python data structures.

dictionary = {}

for i in range(len(l)):

    if( (l[i] in dictionary) == True):
        dictionary[l[i]] = (dictionary[l[i]]+1)

    else:
        dictionary[l[i]] = 1

for i in range(len(l)):
    if dictionary.get(l[i], -1) > 1:
        dictionary.pop(l[i])

dictionary = dict(sorted(dictionary.items()))

print(list(dictionary.keys()))

print(len(dictionary))
