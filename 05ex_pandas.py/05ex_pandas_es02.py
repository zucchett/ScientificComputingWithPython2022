import pandas as pd
import numpy as np
data = pd.read_csv('data/data_000637.txt')
bx = data["BX_COUNTER"]
estimate_bx = max(bx)
print( estimate_bx)