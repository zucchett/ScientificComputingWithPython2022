while True:
    x = input("Please enter first for summing operation: ")
    y = input("Please enter second for summing operation: ")
    try:
            x=int(x)
            y=int(y)
            sum=int(x)+int(y)
            print(sum)
    except:
        try:
            x=float(x)
            y=float(y)
            sum=x+y
            print(sum)
        except:
            try:
                sum=x+y
                print(sum)
            except:
                print("Please try again.")