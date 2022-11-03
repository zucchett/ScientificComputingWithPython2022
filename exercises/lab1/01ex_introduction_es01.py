# The HelloWorld replacement

print("\nExercise 01-a \n")

replacement = []
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("Hello World")
        replacement.append("Hello World")
    elif i%3 == 0:
        print("Hello")
        replacement.append("Hello")
    elif i%5 == 0:
        print("World")
        replacement.append("World")
    else:
        print(i)
        replacement.append(i)

print("\nExercise 01-b \n")

for i in range(len(replacement)):
    if replacement[i] == "Hello":
        replacement[i] = "Python"
    elif replacement[i] == "World":
        replacement[i] = "Works"
result_tuple = tuple(replacement)

print(result_tuple)