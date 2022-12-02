import numpy as np
int_list = list(range(13, 28))

with open("data/data_int.txt", 'w') as output_file1:
    for n in int_list:
        output_file1.write(str(n) + " ")
print("First File: ")
!cat "data/data_int.txt"



float_mat = np.random.random((5, 5)).round(decimals=2)
with open("data/float_int.txt", 'w') as output_file2:
    m,n = float_mat.shape
    for i in range(m):
        for j in range (n):
            if (j != n-1):
                output_file2.write(str(float_mat[i][j]) + " ")
            else:
                output_file2.write(str(float_mat[i][j]))
        output_file2.write("\n")
print("\nSecond File: ")
!cat "data/float_int.txt"


# I think what you mean by "by hand" is not to use csv library
# So I did it by adding ',' to create csv file.
# Obviously using csv library for writing a csv file in another straightforward solution.
with open("data/float_int.csv", 'w') as output_file3:
    with open("data/float_int.txt", 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            line = line.replace(' ',',') + "\n"
            output_file3.write(line)
            
print("\nThird File: ")
!cat "data/float_int.csv"