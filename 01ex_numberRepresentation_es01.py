#part_a
#prints the numbers from 1 to 100
print('numbers from 1 to 100')
for i in range(1, 101):
    print(i)

    
#for multiples of three print "Hello" instead of the number and for the multiples of five print "World"
print('\nmultiples of three print "Hello" instead of the number and for the multiples of five print "World"')
for i in range(1, 101):
    if i%3 == 0 :
        print('Hello')
    elif i%5 == 0:
        print('World')
    else:
        print(i)

#for numbers which are multiples of both three and five print "HelloWorld"
print('\nfor numbers which are multiples of both three and five print "HelloWorld"')
for i in range(1, 101):
    if i% (3*5) == 0:
        print('HelloWorld')  
    elif i%3 == 0 :
        print('Hello')
    elif i%5 == 0:
        print('World')
    else:
        print(i)

#part_b
#Putting the result in a tuple :
result_tuple=()
for i in range(1, 101):
    if i% (3*5) == 0:
        result_tuple = result_tuple + ('HelloWorld',) 
    elif i%3 == 0 :
        result_tuple = result_tuple + ('Hello',)  
    elif i%5 == 0:
        result_tuple = result_tuple + ('World',)
    else:
        result_tuple = result_tuple + (i,)
#substitute "Hello" with "Python" and "World" with "Works"
result_list = list (result_tuple)

for i in range(len(result_list)):
    if result_list[i] == 'Hello':
        result_list[i] = 'Python'
    if result_list[i] == 'World':
    	result_list[i] = 'Works'
    	
print('\nafter substituting "Hello" with "Python" and "World" with "Works": ', result_list)
        
        
