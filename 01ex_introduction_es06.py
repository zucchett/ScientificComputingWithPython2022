from sqlalchemy import true


a = input("Var_1: ")
b = input("Var_2: ")

check = "true"

for i in a:

    if ord(i) < 48 or ord(i) > 57:
        if ord(i) != 46:
            check = "false"
            break
if check == "true":
    a = float(a)


check = "true"
for i in b:

    if ord(i) < 48 or ord(i) > 57:
        if ord(i) != 46:
            check = "false"
            break
# print(check)
if check == "true":
    b = float(b)

try:
  print(a + b)
except:
  print("addention is not possible!!!!!")