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


printEs1=active  #esercizio 3.1
printEs2=passive  #esercizio 3.2
printEs3=passive  #esercizio 3.3
printEs4=passive  #esercizio 3.4
printEs5=passive  #esercizio 3.5
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


#***************************************************Ex 3.3
if(printEs3):
    print("\n\n***************************************************Ex 3.3")


#***************************************************Ex 3.4
if(printEs4):
    print("\n\n***************************************************Ex 3.4")


#***************************************************Ex 3.5
if(printEs5):
    print("\n\n***************************************************Ex 3.5")


#***************************************************Ex 3.6
if(printEs6):
    print("\n\n***************************************************Ex 3.6")

   
#***************************************************Ex 3.7
if(printEs7):
    print("\n\n***************************************************Ex 3.7")
