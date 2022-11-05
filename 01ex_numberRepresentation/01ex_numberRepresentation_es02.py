''' Created by Pedram on 10/19/2022 AD. '''

# Input Two Variables
first = input('First Input =?\n')
second = input('Second Input =?\n')
print("Before Swap -> ","X=",first, "Y=", second)

# Swap Two Variables without Temp Variable
first, second= second, first
print("After Swap -> ","X=",first, "Y=", second)