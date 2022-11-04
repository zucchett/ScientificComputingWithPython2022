Val1 = input("Please enter first value: ")
Val2 = input("Please enter second value: ")
try:
    x = float(Val1)
    y = float(Val2)
    summ = x + y
    print("Sum of entered valuse is: ", summ)
except:
    print('it is not possible to sum these two variable')
