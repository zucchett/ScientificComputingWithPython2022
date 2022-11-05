a = input ("plz enter first element:")
b= input ("plz enter second element:")
a.isdigit()
try:
    c = float(a)+float(b)
    print(c)
except:
    print("sum is not possible")
