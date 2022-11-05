# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:03:59 2022

@author: Ruben
"""

def conv(a, typ):
    
    if a[1] == "b":
        c=int(a[2:], 2) 
    elif a[1] == "x":
        c=int(a[2:], 16)
    else: c=int(a)
    
    if typ=="dec":          
        r=c
    elif typ=="bin":
        r=bin(c)
    elif typ=="hex":
        r=hex(c)
    #else: r="Invalid argument!\n"
    
    return r

while True:
    a=input("Enter the number to be converted \n")
    typ=input("Enter\n dec for decimal representation\n bin for binary representation\n hex for hexadecimal representation\n" )
    try: 
        print(conv(a,typ))
        break
    except ValueError:
        print("\nPlease enter a valid number!")
    except UnboundLocalError:
        print("\nPlease enter a valid argument!\n")

'''while True:
    typ=input("Enter\n dec for decimal representation\n bin for binary representation\n hex for hexadecimal representation\n" )
 
    if conv(a,typ)!="Invalid argument!\n":
        print(conv(a,typ))
        break
    else:
        print("\nInvalid argument!\n")
        
'''    