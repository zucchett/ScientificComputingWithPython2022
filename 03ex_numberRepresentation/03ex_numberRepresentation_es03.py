undflow = 1
ovflow = 1
for i in range(1023):
    undflow = undflow / 2
    ovflow  = ovflow  * 2
scientific_underflow="{:e}".format(undflow)
scientific_overflow="{:e}".format(ovflow)
print(f'\nThe over flow is: {scientific_overflow}')
print(f'The under flow is: {scientific_underflow}')
