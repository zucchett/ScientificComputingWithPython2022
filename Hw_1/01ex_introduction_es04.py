message = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
message= message.lower()
counter = {}

message1 = "The quick brown fox jumps over the lazy dog"
message1= message1.lower()
counter1 = {}
  
for i in message:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
 
for i in message1:
    if i in counter1:
        counter1[i] += 1
    else:
        counter1[i] = 1
  
# printing result 
print ("Count of all characters in S1 \n" + str(counter) + "\n")

print ("Count of all characters in S2 \n" + str(counter1))