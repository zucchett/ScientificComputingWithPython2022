i, first, second, length = 0, 0, 1, 20
           
while(i < length):
    if(i <= 1):
        count = i
    else:
        count = first + second
        first = second
        second = count
    print(count)
    i += 1