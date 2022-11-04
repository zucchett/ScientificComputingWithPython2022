First = 0
Second = 1
           
for Num in range(0, 20):
    if(Num <= 1):
        Next = Num
    else:
        Next = First + Second
        First = Second
        Second = Next
    print(Next)