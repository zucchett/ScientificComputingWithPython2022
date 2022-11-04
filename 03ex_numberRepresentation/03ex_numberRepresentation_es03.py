underflow = 1.0
overflow = 1.0
up_limit = False
down_limit = False

while up_limit == False:
    new = overflow*2
    if new == float('inf'):
        up_limit = True
    else:
        overflow = new

print('The overflow limit is : ', overflow)

while down_limit == False:
    new = underflow/2
    if new == float(0.0):
        down_limit = True
    else:
        underflow = new

print('The underflow limit is: ', underflow)
