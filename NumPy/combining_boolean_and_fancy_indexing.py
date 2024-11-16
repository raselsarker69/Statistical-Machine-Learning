# Combining Boolean and Fancy Indexing
import numpy as np

array = np.array([10, 15, 20, 25, 30])

# Boolean condition combined with specific indices
result = array[(array > 10) & (array < 30)][[0, 2]]   # first part is boolien and second part is fancy.

print('Combined Boolean and Fancy Indexing Result:', result)