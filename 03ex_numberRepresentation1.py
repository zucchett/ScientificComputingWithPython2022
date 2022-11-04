
def convert(n=int,out=str):
  if out in ["bin","int","hex"]:
    out=eval(out)
    print(out(n))

n = input("Please write the number you want to convert: ")
out=input("Please write the output you want to convert the number too: ")

convert(int(n),out)