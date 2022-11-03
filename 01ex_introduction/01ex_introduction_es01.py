list_A= []
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0 :
        list_A.append('HelloWorld')
    elif i % 3 == 0 :
        list_A.append("Hello")
    elif i % 5 == 0 :
        list_A.append("World")
    else :
        list_A.append(i)
print(f'the result for part A is : {tuple(list_A)}')

print('--------------------------------------------------------------------------------------------------')

for i in range(0,len(list_A)) :
    if list_A[i] == 'Hello' :
        list_A[i] = 'Python'
    elif list_A[i] =='World' :
        list_A[i] = 'Works'
    elif list_A[i] =='HelloWorld':
        list_A[i] = 'pythonworks'
    else :
        continue    
print(f'the result for part B is : {tuple(list_A)}')       