first_v = input("Enter the first variable:")
second_v = input("Enter the second variable:")

try:
    total_v = int(first_v) + int (second_v)
    print(total_v)
except:
        try:
            total_v = float(first_v) + float(second_v)
            print(total_v)
        except:
            total_v = first_v + second_v
            print(total_v)