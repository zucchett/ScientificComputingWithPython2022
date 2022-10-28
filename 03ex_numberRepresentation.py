# 03ex - FILE UNICO
#Author: Riccardo Mosele 2044736
import math

#flag per l'esecuzione singola degli esercizi
active = True
passive = False



#SELEZIONARE L'ESERCIZIO DA ESEGUIRE 
#INSERIRE "active" PER ESEGUIRLO
#INSERIRE "passive" PER NON ESEGUIRLO
#E' POSSIBILE L'ESECUZIONE MULTIPLA E DI TUTTI GLI ESERCIZI


printEs1=passive  #esercizio 3.1
printEs2=passive  #esercizio 3.2
printEs3=passive  #esercizio 3.3
printEs4=passive  #esercizio 3.4
printEs5=active  #esercizio 3.5
printEs6=passive  #esercizio 3.6
printEs7=passive  #esercizio 3.7



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
0x65ba58f0

#***************************************************Ex 3.4
if(printEs4):
    print("\n\n***************************************************Ex 3.4")


#***************************************************Ex 3.5
import math
if(printEs5):
    print("\n\n***************************************************Ex 3.5")

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

    res1 = quadratic_equation(0.001,1000,0.001)
    res2 = quadratic_equation2(0.001,1000,0.001)

    print(f"Res1_a: {res1[0]}\nRes1_b: {res2[0]}")
    print(f"\nRes2_a: {res1[1]}\nRes2_b: {res2[1]}")

    print("\nx^2+2x+2 -> a=1, b=2, c=2")
    res_c = quadratic_equation(1,2,2)
    print(f"Complex res 1: {res_c[0]}\nComplex res 2: {res_c[1]}")

#***************************************************Ex 3.6
if(printEs6):
    print("\n\n***************************************************Ex 3.6")

   
#***************************************************Ex 3.7
if(printEs7):
    print("\n\n***************************************************Ex 3.7")
