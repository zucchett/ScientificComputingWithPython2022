#!wget https://www.dropbox.com/s/8m0syw2tkul3dap/credit_card.dat  -P ./data/
with open('data/credit_card.dat','rb') as dat_file:
    lines = dat_file.readlines()
    word_size = 6
    cards = []
    for line in lines:
        if (len(line) >= 19*6):
            counter = 0
            s = ''
            for i in range(2, 120, word_size):
                counter += 1
                if (counter % 5 !=0):
                    num = int(line[i : i+word_size-2], 2)
                    s += str(num)
                else:
                    s += ' '
            cards.append(s)

for card in cards:
    print(card)