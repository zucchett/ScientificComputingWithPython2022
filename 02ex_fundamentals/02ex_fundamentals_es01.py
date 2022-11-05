#ex_01
#Convert the function into a function that doesn't use global variables and that does not modify the original list

#x = 5 = variabile globale 

#f(alist) aggiunge alla lista originale tutti i numeri da 0 a 4. Io devo scrivere una funzione che non modifichi 
#la lista originale e usi variabili locali 

def f(alist,x):

    for i in range(5):
        alist = alist + [i,]
    return alist

alist = [1, 2, 3]

ans = f(alist,x)

print(ans)
print(alist) # alist has been changed

