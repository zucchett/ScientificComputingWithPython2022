##Counting Letters
map_of_characters = {}
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

print(s1.lower().rstrip())

# for c in s1 : 
#   print(c)
for character in s1.lower().rstrip():
  map_of_characters[character] = map_of_characters.get(character,0) + 1

for k in map_of_characters:
  print("Character :"+k ,"is repeated %d times" % map_of_characters[k])

print("========================================================")
print("In string 2 we have those informations about character repetition :")

map_of_characters2 = {}
for character in s2.lower().rstrip():
  map_of_characters2[character] = map_of_characters2.get(character,0) + 1

for k in map_of_characters2:
  print("Character :"+k ,"is repeated %d times" % map_of_characters2[k])

