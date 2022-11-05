def shorter_words(x , n):
    new_list = list(filter(lambda v: len(v)<n, x))
    return new_list

x = ['Mofmfglmpfg','Ha','R','D','ll','tkmtrmgitrmt']

shorter_words(x , 3)