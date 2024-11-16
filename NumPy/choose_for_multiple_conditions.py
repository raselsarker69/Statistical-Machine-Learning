# Using np.choose for Multiple Conditions
import numpy as np

# Creating arrays for conditions
array = np.array([0, 1, 2, 3])  # Now we have 0, 1, 2, 3 as possible indices

# Add a fourth array to choices
choices = [array * 2, array + 10, array ** 2, array - 5]  # array - 5 means index 3

# Using np.choose to apply different conditions
result = np.choose(array, choices)

print('Result using np.choose:', result)
