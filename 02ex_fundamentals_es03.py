letters = []


print("getting words...", "\n")
print("enter '0' as you finisht")

while True:
    a = input("enter word: ")
    if a == "0":
        break
    letters.append(a)

print("getting enteger n...", "\n")
n = int(input("enter n: "))

result = list(filter(lambda x: len(x) <= n, letters)) 
  
# printing the result
print(result) 
