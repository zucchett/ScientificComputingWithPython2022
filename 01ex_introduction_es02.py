# x=input('enter value of x:')
# y=input('enter value of y:')
# # create a temporary variable and swap the values
# temp=x
# x=y
# y=temp
# print(f'the value of x after swapping:{x}')
# print(f'the value of y after swapping:{y}')


from re import X


x=input('enter value of x:')
y=input('enter value of y:')
x,y=y,x   #without the use of any temporary variable
print('x=',x)
print('y=',y)