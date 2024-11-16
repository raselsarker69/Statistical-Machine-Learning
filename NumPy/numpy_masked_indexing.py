# Masked Indexing
import numpy as np

# Creating an array
array = np.array([1, -2, 3, -4, 5])

# Creating a mask for positive values
mask = array > 0
mask_neg = array < 0

# Applying mask to get only positive values
positive_values = array[mask]
negative_values = array[mask_neg]

print('Positive Values:', positive_values)
print('Negative Values:', negative_values)