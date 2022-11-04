# 6. Casting

x = input("\nEnter the variable x:")
y = input("\nEnter the variable y:")

# import sys

# x = sys.argv[1] 
# y = sys.argv[2]

try:
    sum = float(x)+float(y)
    print(sum)
except:
    try:
        print(x+y)
    except:
        print('\nThis should not be possible!')