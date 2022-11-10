lst=[]
tpl=()
x = 0
while x<100:
   x += 1 
   if x % 3 == 0 and x % 5 == 0:
       a = "hello world"
   elif x % 3 == 0:
       a = "hello"
   elif x % 5 == 0:
       a = "world"
   else: 
       a = x
   print (a) 
   tpl=tpl+(a,) 

lst = list(tpl)   # in order to make changes on tuple we change it to list
b=0
while b<100:
    if lst[b]=="hello":
        lst[b]="python"
    elif lst[b]=="world":
        lst[b]="works"
    b += 1 

tpl=tuple(lst)  # finally we change the list to a tuple

print(tpl)
