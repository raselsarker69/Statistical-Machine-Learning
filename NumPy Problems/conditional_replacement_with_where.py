# Conditional Replacement with np.where
import numpy as np

# Creating an array
array = np.array([10, 15, 20, 25, 30])

# Replacing values based on condition
result = np.where(array > 20, 0, array)   # 20 ar chaya big value gulo replace by 0

print('Array with Values Greater Than 20 Replaced with 0:', result)