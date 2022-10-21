# 02ex - FILE UNICO
#Author: Riccardo Mosele 2044736
import math

#flag per l'esecuzione singola degli esercizi
active = True
passive = False



#SELEZIONARE L'ESERCIZIO DA ESEGUIRE 
#INSERIRE "active" PER ESEGUIRLO
#INSERIRE "passive" PER NON ESEGUIRLO
#E' POSSIBILE L'ESECUZIONE MULTIPLA E DI TUTTI GLI ESERCIZI


printEs1=passive  #esercizio 2.1
printEs2=passive  #esercizio 2.2
printEs3=passive  #esercizio 2.3
printEs4=passive  #esercizio 2.4
printEs5=passive  #esercizio 2.5
printEs6=passive  #esercizio 2.6
printEs7=passive  #esercizio 2.7
printEs8=passive  #esercizio 2.8
printEs9=passive  #esercizio 2.9
printEs10=passive #esercizio 2.10
printEs11=passive #esercizio 2.11



#***************************************************Ex 2.1
if(printEs1):
    print("\n\n***************************************************Ex 2.1")

    def f(alist, x):
        tmpList=[i for i in alist]
        for i in range(x):
            tmpList.append(i)
        return tmpList

    alist = [1, 2, 3]
    ans = f(alist, 5)
    print(ans)
    print(alist) # alist has not been changed


#***************************************************Ex 2.2
if(printEs2):
    print("\n\n***************************************************Ex 2.2")

    ans = list(map(lambda x: x * x,
    filter(lambda x: x % 2 == 1, range(10))))
    print(f"With map and filter:\n{ans}")

    list=[x*x for x in range(10) if x % 2 == 1]
    print(f"\nWith list List comprehension:\n{list}")

#***************************************************Ex 2.3
if(printEs3):
    print("\n\n***************************************************Ex 2.3")


    listWord = ["Ciao", "Buongiorno", "Buonasera", "Buonanotte", "Salve"]
    
    try:
        x = int(input("Insert the max lenght: "))
        res=[]
        for i in filter(lambda y: len(y)<int(x), listWord):
            res.append(i)
        print(res)
    except:
        print("ERROR: Insert an integer value!")

    
#***************************************************Ex 2.4
if(printEs4):
    print("\n\n***************************************************Ex 2.4")

    lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
    print(f"length of the keys: {list(map(lambda y: len(y),lang))}")

#***************************************************Ex 2.5
if(printEs5):
    print("\n\n***************************************************Ex 2.5")

    language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

    language_scores.sort(key = lambda x: x[0])
    print(f"Alphabetical order of first element: \n{language_scores}")


#***************************************************Ex 2.6
if(printEs6):
    print("\n\n***************************************************Ex 2.6")

    def square(a):
        return a*a

    def cube(b):
        return b*b*b

    def sixth(c):
        return square(cube(c))

    print(f"two at 6th power: {sixth(2)}")


#***************************************************Ex 2.7
if(printEs7):
    print("\n\n***************************************************Ex 2.7")


#***************************************************Ex 2.8
if(printEs8):
    print("\n\n***************************************************Ex 2.8")


#***************************************************Ex 2.9
if(printEs9):
    print("\n\n***************************************************Ex 2.9")


#***************************************************Ex 2.10
if(printEs10):
    print("\n\n***************************************************Ex 2.10")


#***************************************************Ex 2.11
if(printEs11):
    print("\n\n***************************************************Ex 2.11")
