import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Modifying elements at indices 0 and 1
array[[0, 1]] = [100, 200]

print(array)
