#3. Underflow and overflow


underflow=1.0
overflow=1.0

while True:
  o= overflow
  overflow=overflow*2
  if str(overflow)== "inf":
    print("The overflow limit of floating points is:",o)
    break

while True:
  u= underflow
  underflow=underflow / 2
  if underflow == 0.0:
    print("The underflow limit of floating points is:",u)
    break
