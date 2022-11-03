def wrods_less_than_n (alist,n):
    print(list(filter(lambda x: len(x)<n , alist)))
    
alist = ["Hello","Good Morning","Bye","Ciao", "Buonanotte"]
n = 5

wrods_less_than_n(alist,n)