x1=input("Please write the first value:")
x2=input("Please write the second value")


try:
    x1=float(x1)
    x2=float(x2)
    print("The sum of two variables is ",float(x1)+float(x2))
except:
    print("Sorry you write a string,please enter two number")