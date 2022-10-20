# 01ex - FILE UNICO
#Author: Riccardo Mosele 2044736
import math

#flag per l'esecuzione singola degli esercizi
active = True
passive = False



#SELEZIONARE L'ESERCIZIO DA ESEGUIRE 
#INSERIRE "active" PER ESEGUIRLO
#INSERIRE "passive" PER NON ESEGUIRLO
#E' POSSIBILE L'ESECUZIONE MULTIPLA E DI TUTTI GLI ESERCIZI


printEs1=active  #esercizio 1.1
printEs2=active  #esercizio 1.2
printEs3=active  #esercizio 1.3
printEs4=active  #esercizio 1.4
printEs5=active  #esercizio 1.5
printEs6=active  #esercizio 1.6
printEs7=active  #esercizio 1.7
printEs8=active  #esercizio 1.8
printEs9=active  #esercizio 1.9
printEs10=active #esercizio 1.10
printEs11=active #esercizio 1.11



#***************************************************Ex 1.1
if(printEs1):
    print("\n\n***************************************************Ex 1.1")

    listaTest=[]

    for x in range(1,101,1):
        #se il valore è divisibile per 5 e per 3
        if (x%3==0 and x%5==0):
            listaTest.append("HelloWorld")
            #print("HelloWorld")
    
        #se il valore è divisibile per 3
        elif x%3==0:
            listaTest.append("Hello")
            #print("Hello")

        #se il valore è divisibile per 5
        elif x%5==0:
            listaTest.append("World")
            #print("World")

        #altrimenti inserisco il numero
        else: 
            listaTest.append(x)
            #print(x) 

    for i in range(len(listaTest)):
        if (listaTest[i]=="Hello"):
            listaTest[i]="Python"
        elif (listaTest[i]=="World"):
            listaTest[i]="Works"

    #converto la lista in una tupla e stampo il risultato
    tuplaResut = (tuple(listaTest))
    print(tuplaResut)

#***************************************************Ex 1.2
if(printEs2):
    print("\n\n***************************************************Ex 1.2")
    #inserisco i valori terminale
    x = input('insert X: ')
    y = input('insert Y: ')

    #faccio lo swap senza variabile temporanea
    x, y = y, x

    print("x =", x)
    print("y =", y)

#***************************************************Ex 1.3
if(printEs3):
    print("\n\n***************************************************Ex 1.3")

    #funzione che calcola la distanza euclidea tra due vettori bidimensionali u e v
    def computingDistance(u,v):
        return math.sqrt((v[0]-u[0])**2+((v[1]-u[1]))**2)
    
    #inserisco i valori da terminale
    x1 = input('insert x1: ')
    y1 = input('insert y1: ')
    x2 = input('insert x2: ')
    y2 = input('insert y2: ')

    #inserisco i valori in due tuple, se non sono numeri interi restituisco un messaggio d'errore
    try:
        u=(int(x1),int(y1))
        v=(int(x2),int(y2))
        res = computingDistance(u,v)
        print(f"Euclideam distance: {res}")
    except:
        print("Error: value are not accept")

#***************************************************Ex 1.4
if(printEs4):
    print("\n\n***************************************************Ex 1.4")

    #funzione che conta e stampa le occorrenze di una stringa m
    def countingLetters(m):

        print("String:\n"+m+"\n")

        #ignoro i caratteri maiuscoli
        s = m.lower() 
        occ={}  

        #tramite un dizionario salvo le occorrenze di ogni carattere presente nella stringa
        for char in s:
            occ[char]=s.count(char)
        print(f"Occurs: {occ}")

        
    s1 = "Write a program that prints the numbers from 1 to 100. \
    But for multiples of three print Hello instead of the number and for the multiples of five print World. \
    For numbers Which are multiples of both three and five print HelloWorld."
    s2 = "The quick brown fox jumps over the lazy dog"
    s3 = "aaaabbbb cccc dd"

    countingLetters(s1)

#***************************************************Ex 1.5
if(printEs5):
    print("\n\n***************************************************Ex 1.5")

    l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
    85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
    1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
    45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
    

    unique_numbers = {}
    not_unique_numbers={}

    #con l'ausilio di un dizionario conto e salvo i numeri presenti e le relative occorrenze
    #in unique_numbers se sono unici
    #in not_unique_numbers se sono più di uno
    for i in l:
        if not i in not_unique_numbers:
            if l.count(i) == 1:
                unique_numbers[i] = l.count(i)
            else:
                not_unique_numbers[i] = l.count(i)
    print(f"Unique numbers are: {len(unique_numbers)}")
    print(unique_numbers)
    
#***************************************************Ex 1.6
if(printEs6):
    print("\n\n***************************************************Ex 1.6")

    #inserisco i valori da terminale
    x = input("Please enter first integer, float or string value: ")
    y = input("Please enter second integer, float or string value: ")
    
    #faccio il cast a float, se non viene lanciata un'eccezione sommo i due valori
    #-->float include anche gli int
    try:
        res=float(x)+float(y)
        print(res)

    #se è una stringa stampo l'errore
    except:
        print("ERROR: Sum is not possible!")
   
#***************************************************Ex 1.7
if(printEs7):
    print("\n\n***************************************************Ex 1.7")

    #lista di cubi utilizzando un ciclo for
    listCubicLoop=[]
    for i in range(10):
        listCubicLoop.append(i**3)
    print(f"With for cycle: {listCubicLoop}")

    #lista di cubi utilizzando le list comprehension
    listCubicCompr = [i**3 for i in range(10)]
    print(f"With list comprehension: {listCubicCompr}")

#***************************************************Ex 1.8
if(printEs8):
    print("\n\n***************************************************Ex 1.8")

    #codice da copiare utilizzando le list comprehension
    a = []
    for i in range(3):
        for j in range(4):
            a.append((i, j))
    print(f"With for loop: \n{a}")

    #utilizzando le list comprehension
    a_compr = [(x, y) for x in range(3) for y in range(4)]
    print(f"With list comprehension: \n{a_compr}")

#***************************************************Ex 1.9
if(printEs9):
    print("\n\n***************************************************Ex 1.9")

    listPy=[]
    c, m = 0, 2
 
    #99 è il limite impostato
    while c < 99 :
        
        for n in range(1, m+1) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            if c > 99 :
                break
            if(a==0 or b==0 or c==0):
                break

            listPy.append((a,b,c))
 
        m = m + 1
    
    #converto la lista in una tupla
    tuplaPy = (tuple(listPy))
    print(tuplaPy)

#***************************************************Ex 1.10
if(printEs10):
    print("\n\n***************************************************Ex 1.10")

    #lista di numeri casuale
    numbers=[5,16,458,102,27,65,31,2,48,124,57]
    print(f"Original numbers are:\n{numbers}")

    norm=0

    #calcolo la norma per la lista di numeri
    for i in numbers:
        norm = norm + i**2
    norm = math.sqrt(norm)

    #normalizzo i numeri della lista
    for n in range(len(numbers)):
        numbers[n] = numbers[n]/norm
    
    print(f"\nNormalize numbers are:\n{numbers}")

    #verifico che la somma dei quadrati sia zero
    sum=0
    for s in range(len(numbers)):
        sum = sum+numbers[s]**2
    print(f"\nThe sum of normalized number are:\n{sum}")

#***************************************************Ex 1.11
if(printEs11):
    print("\n\n***************************************************Ex 1.11")

    #i primi due valori della serie di fibonacci sono statici, rispettivamente 1, 1
    fibSeq=[1,1]

    #calcolo i successivi 18 valori utilizzando solo il ciclo for
    for i in range(18):
        fibSeq.append(fibSeq[len(fibSeq)-1]+fibSeq[len(fibSeq)-2])

    print(f"First 20 numbers of the Fibonacci sequence:\n{fibSeq}")
