# 1. Number representation
# Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex). 
# Determine the input type in the function, and pass another argument to choose the output representation.

def convert(n=int,out=str):
  if out in ["bin","int","hex"]:
    # print(out(n))
    out=eval(out)
    print(out(n))

n = input("Enter the number you want to convert: ")
out=input("Enter the output you want to convert the number too: ")

convert(int(n),out)