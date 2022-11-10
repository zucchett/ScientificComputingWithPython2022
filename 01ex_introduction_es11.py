# #if n=0 Fn=0, if n=1 Fn=1, if n>1 Fn = Fn-1 + Fn-2
number=int(input('arbitary term'))
firstvalue=0
secondvalue=1
i=0
while i<number:
    print(firstvalue)
    next=firstvalue+secondvalue
    # update values
    firstvalue=secondvalue
    secondvalue=next
    i+=1
