
undflow = 1
ovflow = 1
for i in range(1023):
    undflow = undflow / 2
    ovflow  = ovflow  * 2
scientific_undflow="{:e}".format(undflow)
scientific_ovflow="{:e}".format(ovflow)
print(f'\nThe over flow is: {scientific_ovflow}')
print(f'The under flow is: {scientific_undflow}')
print(f'I do the loop for 1023 times to reach the overflow and underflow.\n')