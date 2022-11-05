def is_shorter(lista,n):
    return len(lista)< n 
ls=["sdaf","df","ghj","h","fghjk","ghdfjnb"]

print(list(filter(lambda lis:is_shorter(lis,3), ls)))