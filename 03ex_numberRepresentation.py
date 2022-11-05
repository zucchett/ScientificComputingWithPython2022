# 03ex - FILE UNICO
#Author: Riccardo Mosele 2044736
#flag per l'esecuzione singola degli esercizi
active = True
passive = False



#SELEZIONARE L'ESERCIZIO DA ESEGUIRE 
#INSERIRE "active" PER ESEGUIRLO
#INSERIRE "passive" PER NON ESEGUIRLO
#E' POSSIBILE L'ESECUZIONE MULTIPLA E DI TUTTI GLI ESERCIZI


printEs1=active  #esercizio 3.1
printEs2=active  #esercizio 3.2
printEs3=active  #esercizio 3.3
printEs4=active  #esercizio 3.4
printEs5=active  #esercizio 3.5
printEs6=active  #esercizio 3.6
printEs7=active  #esercizio 3.7


import math
import timeit

#***************************************************Ex 3.1
if(printEs1):
    print("\n\n***************************************************Ex 3.1")

    def convert_num(data, finalType):
        #controllo che l'inserimento per il tipo di output sia corretto (solo H, D o B)
        if(not(finalType=="B" or finalType=="D" or finalType=="H")):
            print("ERROR: wrong value for OUTPUT")
            return

        #se l'inserimento del tipo di output è corretto proseguo
        if data[0:2] == "0x": #caso esadecimale
            try:
                #controllo che il valore inserito sia effettivamente un numero
                data=int(data, 16)
                print("(input is hex)")
            except:
                print("ERROR: wrong value")
                return

        elif data[0:2] == "0b": #caso binario
            try:
                #controllo che il valore inserito sia effettivamente un numero
                data=int(data, 2)
                print("(input is bin)")
            except:
                print("ERROR: wrong value")
                return
        else: #caso decimale
            try:
                #controllo che il valore inserito sia effettivamente un numero
                data=int(data)
                print("(input is dec)")

            except:
                print("ERROR: wrong value")
                return

        #converto il numero inserito nel rispettivo formato
        if(finalType=="D"): #caso decimale
            return(int(data))
        elif(finalType=="H"): #caso esadecimale
            return(hex(data))
        else:
            return(bin(data)) #caso binario


    x=input("Insert Value (Bin, Hex or Int): ")
    outputVal=input("Insert output base \"B\" for bin, \"H\" for hex and \"D\" for dec: ")
    print(f"\nOutput value: {convert_num(x,outputVal)}")

#***************************************************Ex 3.2
if(printEs2):
    print("\n\n***************************************************Ex 3.2")

    def convert_func(val):
        try:
            sign = int(val[0])          # segno, 1 bit
            exp = int(val[1:9],2)       # esponente, 8 bits
            mant = int("1"+val[9:], 2)  # mantissa, len(val)-9 bits
            return (-1)**sign * mant /( 1<<( len(val)-9 - (exp-127) ))
            
        except:
            print("ERROR!")

    number = "110000101011000000000000" 
    print(f"Single precision floating point in decimal representation: {convert_func(number)}") 

#***************************************************Ex 3.3
if(printEs3):
    print("\n\n***************************************************Ex 3.3")

    overflow_val = 1.0
    underflow_val = 1.0
    
    #overflow: moltiplico il valore iniziale per due fino a che non viene assegnato a infinito -> overflow
    while True:
        overflow_val = overflow_val * 2
        if math.isinf(overflow_val *2):
            break

    #underflow: divido il valore iniziale per due fino a che non risulta zero -> underflow
    while True:
        underflow_val = underflow_val / 2
        if underflow_val/2 == 0:
            break

    print(f"Overflow value is: {overflow_val}")
    print(f"Underflow value is: {underflow_val}")

#***************************************************Ex 3.4
if(printEs4):
    print("\n\n***************************************************Ex 3.4")

    #definisco valore e incremento iniziale
    y=0.1
    res=1
    while(res != res+y):
        #continuo a dimezzare il valore fino a che non ha più effetto
        y=y/2

    print(f"The machine precision for floating point numbers is: {y*2}")
    print(f"\n--> 1 + {y*2} = {1+y*2}")
    print(f"--> 1 + {y} = {1+y}")

#***************************************************Ex 3.5
if(printEs5):
    print("\n\n***************************************************Ex 3.5")

    #formula base anche con soluzione complessa
    def quadratic_equation(a,b,c):
        res=[]

        #calcolo il delta
        delta = b**2-4*a*c
        #print(f"Delta: {delta}\n")

        try:
            if(delta<0): #se minore di zero ho due risultati complessi
                firstTerm=-b/2*a
                secondTerm=math.sqrt(-delta)/(2*a)
                res.append(str(firstTerm)+"+"+str(secondTerm)+"i")
                res.append(str(firstTerm)+"-"+str(secondTerm)+"i")
                return res

            else: #altrimenti calcolo il valore finale di entrambi
                res.append((-b+math.sqrt(delta))/(2*a))
                res.append((-b-math.sqrt(delta))/(2*a))
                return res
        except:
            print("ERROR!")
            return

    #soluzione con moltiplicazione di -b mp rad(b^2-4ac)
    def quadratic_equation2(a,b,c):
        res=[]

        #controllo che il delta sia maggiore di zero
        delta = b**2-4*a*c
        #print(f"Delta: {delta}\n")
        if(delta<0):
            print("Not real solution")
            return

        try:
            #calcolo i due risultati
            res.append(((-b+math.sqrt(delta))*(-b-math.sqrt(delta)))/((2*a)*(-b-math.sqrt(delta))))
            res.append(((-b-math.sqrt(delta))*(-b+math.sqrt(delta)))/((2*a)*(-b+math.sqrt(delta))))
            return res

        except:
            print("ERROR!")
            return

    #soluzione standard con delta>0 e valori forniti
    res1 = quadratic_equation(0.001,1000,0.001)

    #soluzione con la moltiplicazione fornita
    res2 = quadratic_equation2(0.001,1000,0.001)

    #stampo il confronto
    print(f"Res1_a: {res1[0]}\nRes1_b: {res2[0]}")
    print(f"\nRes2_a: {res1[1]}\nRes2_b: {res2[1]}")
    #--> moltiplicando e poi dividendo il risultato per lo stesso numero otteniamo un numero appena 
    #--> diverso da quello originale, teoricamente il risultato non dovrebbe cambiare. In pratica
    #--> potrebbe essere diverso a causa del numero limitato di cifre decimali per i float, vengono quindi
    #--> introdotti degli errori di arrotondamento


    #test di una soluzione complessa con a=1, b=2, c=2
    print("\nx^2+2x+2 -> a=1, b=2, c=2")
    res_c = quadratic_equation(1,2,2)
    print(f"Complex res 1: {res_c[0]}\nComplex res 2: {res_c[1]}")

#***************************************************Ex 3.6
if(printEs6):
    print("\n\n***************************************************Ex 3.6")

    #funzione f(x)
    def func_x(x):
        return x*(x-1)

    #derivata della funzione f(x)
    def deriv_x(y,delta):
        return (func_x(y+delta)-func_x(y))/delta

    print(f"Derivative with delta=10^-2 (for x=1): {deriv_x(1,10**-2)}")
    print(f"Derivative calculate analytically (for x=1): {float(1)}\n") #analiticamente: df(x)=2x-1
    #--> i due valori non coincidono perfettamente perchè il delta con cui stiamo calcolando la derivata non è esattamente zero. 

    #calcolo il valore della derivata cambiando il delta: 10^ -> -4,-6,-8,-10,-12,-14
    for i in range(4,15,2):
        print(f"Derivative with delta=10^{-i} (for x=1): {deriv_x(1,10**-i)}")
    #--> l'accuratezza del delta aumenta fino al valore 10^-8 dopo inizia a decrescere.

#***************************************************Ex 3.7
if(printEs7):
    print("\n\n***************************************************Ex 3.7")

    def semicircle(x): 
        return math.sqrt(1-x*x) 

    #calcolo l'integrale della funzione func
    def integrate(func, a, b, N): 
        d = (b - a) * 1.0 / N 
        return d*(0.5*func(a) + sum(func(a+i*d) for i in range(1, N)) + 0.5*func(b)) 
 
    N=100
    print(f"Integral with N=100: {integrate(semicircle, -1, 1, N)}") 
    print(f"Original result: {1.57079632679}")
    #--> the result calculated by me with N = 100 is less accurate by at least 0.01

    #calcolo con quanti N la funzione ci impiega a essere eseguita
    N=5000000 #dopo vari test parto da un numero già elevato
    time=0
    flagTmp=True

    #incremento N fino a che la funzione non impiega più di un secondo
    while(time < 1):
        if(flagTmp):
            print("Wait...")
            flagTmp=False

        time = timeit.timeit(stmt='integrate(semicircle, -1, 1, N)', globals=globals(), number=1)

        if(time<0.5):
            N=N**2
        if(time<0.8):
            N=N*4
        else:
            N=N+100

    print(f"\nN with computation run in less than a second (precision of pm 100):\n--->N: {N}")
    print(f"Integral with N={N}: {integrate(semicircle, -1, 1, N)}") 
    print(f"Original result: {1.57079632679}\n")
    #-->eseguendo per un minuto otteniamo un valore di N che tende a più infinito