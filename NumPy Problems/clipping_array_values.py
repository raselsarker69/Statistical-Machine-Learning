# Clipping Array Values
# Clipping array values in NumPy means setting a minimum and/or maximum limit on the values within an array

import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5])

# Clipping values to be between 2 and 4
clipped_array = np.clip(array, 2, 4)

print('Original Array:', array)
print('Clipped Array:', clipped_array)