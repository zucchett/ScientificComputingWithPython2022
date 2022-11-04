#List comprehension

#ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))

import math
new_ans = [math.pow(x,2) for x in range(10) if x % 2 == 1]
print(new_ans)