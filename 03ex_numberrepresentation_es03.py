
uflow = 1
oflow = 1
sum = 0
for i in range(1023):
    undflow = uflow / 2
    ovflow  = oflow  * 2
    sum  += 1
scientific_uflow="{:e}".format(uflow)
scientific_oflow="{:e}".format(oflow)
print(f'\nThe over flow is: {scientific_oflow}')
print(f'The under flow is: {scientific_uflow}')
print(f'I do the loop for {sum} times to reach the overflow and underflow.\n')