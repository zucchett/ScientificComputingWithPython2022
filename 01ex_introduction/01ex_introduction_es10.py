vector = input('Enter vector elements with a space between them ').split()
N = sum([float(x) for x in vector])
normalized_vector = [float(x)/N for x in vector]
print(normalized_vector)
print('Check the normalized elemnts sum: ', sum(normalized_vector))