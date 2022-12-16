#actually, i need more time to underestand this topic, sorry but i miss the deadline, i write this because it is important for me to inform you this lecture is important for me,and i will be solve my problems as soon as possible


import pandas as pd

import numpy as np
import csv
import math as m

with open('credit_card.dat', 'rb') as file:
    file_content = file.readlines()

    allcarts =[]
    word_counter = 0
    word_size = 8
    total_digitnumber = 16+3
    digit_length = 6


    for row in file_content:

        if(round(len(row)/digit_length) >= total_digitnumber):

            utf_string = row.decode("utf-8")

            utf_string = utf_string[:-4]


            start_index = 0
            card_number=[]

            for i in range(total_digitnumber):
                end_index = start_index + digit_length
                digits_4 = utf_string[start_index:end_index]
                card_number.append(digits_4)
                start_index += digit_length




            credit_card = ""
            for i in range(total_digitnumber):
                credit_card += chr(int(card_number[i],2))

            allcarts.append(credit_card)

    print("Number of all the Credit Card is :\n")
    for i in allcarts:
        print(i, "\n")