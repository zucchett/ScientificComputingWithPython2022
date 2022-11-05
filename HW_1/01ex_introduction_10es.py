# Normalization is rescaling to a rangeof 0 to 1
num = [33, 9.8, 1.2]
norm = [float(i) / sum(num) for i in num]

print(norm)
