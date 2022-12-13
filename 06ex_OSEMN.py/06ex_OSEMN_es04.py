import numpy as np
import pandas as pd
import csv
import json

with open('credit_card.dat','rb') as read_dat:
    line = read_dat.readlines() 
    for row in line:
        if(len(row) > 5): 
            utf_2_strng = row.decode("utf-8")
            utf_2_strng = utf_2_strng[0:114]   
            start_digit = 0
            digit_space = 6
            card_digits=[]
            for i in range(19):
                end_digit = start_digit + digit_space
                digits_4 = utf_2_strng[start_digit:(start_digit + digit_space)]
                card_digits.append(digits_4)
                start_digit = start_digit + digit_space                
            credit_card = ""
            counter = 1
            for i in range(0,19):
                credit_card = credit_card + chr(int(card_digits[i],2))
            print(credit_card)