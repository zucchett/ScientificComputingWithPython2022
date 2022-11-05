out_tuple = ()

for i in [x+1 for x in range(100)]:
    if i%15 == 0:
        
        out_tuple = out_tuple + ('Hello World',)
        print('Hello World')
    elif i%5 == 0:
        out_tuple = out_tuple + ('Works',)
        print('World')
    elif i%3 == 0:
        out_tuple = out_tuple + ('Python',)
        print('Hello')
    else:
        out_tuple = out_tuple + (i,)
        print(i)


print(out_tuple)