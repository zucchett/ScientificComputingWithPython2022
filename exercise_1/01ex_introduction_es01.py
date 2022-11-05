multipleOfThree = 0
x = 1
text = ""
tpl = ()
while x <= 100:
    if x % 3 == 0 and x % 5 == 0:
        text = "HelloWorld"
    elif x % 3 == 0:
        text = "Hello"
    elif x % 5 == 0:
        text = "World"
    else:
        text = x
    print(text)
    tpl = tpl + (text,)
    x += 1

i = 0
lst = list(tpl)
for item in tpl:
    if item == "Hello":
        text = "Python"
    elif item == "World":
        text = "Works"
    else:
        text = item
    lst[i] = text
    tpl = tuple(lst)
    i += 1
print(tpl)
