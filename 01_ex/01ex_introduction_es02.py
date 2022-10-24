tuple = ()
for numtext in range(1, 101):
    if numtext % 3 == 0 and numtext % 5 == 0:
        x = "Hello world"
    elif numtext % 3 == 0:
        x = "Hello"
    elif numtext % 5 == 0:
        x = "world"
    else:
     x = numtext
    print(x)
    tuple= tuple + (x,)
l=list(tuple)

i=0
for item in tuple:
    if item=="Hello":
        x="python"
    elif item=="world":
        x=="works"
    else:
        x=item
    l[i]=x
    tuple=tpl(l)
    i+=1
print(tuple)



