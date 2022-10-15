# 1. The HelloWorld replacement

# a) Write a program that:
#   - prints the numbers from 1 to 100
#   - but for multiples of three print "`Hello`" instead of the number and for the multiples of five print "`World`"
#   - for numbers which are multiples of both three and five print "`HelloWorld`".

numbers = []
for i in range(100):
    if i%5==0 and i%3==0:
        numbers.append("Hello World") 
        print("Hello World") 
    elif i%3==0 :
        numbers.append("Hello")
        print("Hello")
    elif i%5==0: 
        numbers.append("World")
        print("World")
    else:
        numbers.append(i)
        print(i)


# b) Put the result in a tuple and substitute "`Hello`" with "`Python`" and "`World`" with "`Works`".
for i in numbers:
    if numbers[i]=="Hello":
        numbers[i]="Python"
    elif numbers[i]=="World":
        numbers[i]="Works"
    else:
        numbers[i]=i

numbers=tuple(numbers)