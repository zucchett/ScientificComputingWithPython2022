"""
4. Reading the credit card numbers

Get the binary file named credit_card.dat from this address:

https://www.dropbox.com/s/8m0syw2tkul3dap/credit_card.dat
and convert the data into the real credit card number, knowing that:

each line corresponds to a credit card number, which consists of 16 characters (which are numbers in the 0-9 range) divided in 4 blocks, with a whitespace between each block
each character is written using a 6 bit binary representation (including the whitespace)
the final 4 bits of each line are a padding used to determine the end of the line, and can be ignored
Hint: convert the binary numbers to the decimal representation first, and then use the chr() function to convert the latter to a char
"""
import pandas as pd
file_name = 'credit_card.dat'
credit_cards = []
with open(file_name, mode='r') as f:
    for line in f:
        n = 6
        bin_chars = [line[i:i + n] for i in range(0, len(line) - 5, n)]

        card_number = ""
        for char in bin_chars:
            card_number += chr(int(char, 2))

        credit_cards.append(card_number)

print(credit_cards)