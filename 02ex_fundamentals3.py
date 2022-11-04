lista =[]
lista= input("Put an value,please separate with space")
lista = list(filter(None,lista.split(' ')))
print(lista)
try:
    n=int(input("Please give a number"))
    # Solution 1 - With function -->
    def is_short(elements,n):
        return len(elements)<=n
    result1=list(filter(lambda x: is_short(x,n),lista))
    print("The  list of words that are shorter than number you put ",result1)
    #Solution 2 - Without function is_short -->
    result2 =list(filter(lambda x: (len(x)<=n),lista))
    print("The  list of words that are shorter than number you put ",result2)
except:
    print("You have not writen an number, please write a number")
