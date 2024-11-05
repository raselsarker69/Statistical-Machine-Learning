# It is only possible to reshape or reorder the array when it perfectly aligns with the specified structure. Essentially, 
# the array must have the required number of elements to fit into the desired format correctly. If the array does not have 
# an even number of elements or does not meet the specified limit, then it cannot be reshaped and will not fit the intended structure.
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Reshaping the array into a shape that fits 10 elements
reshaped_array = array.reshape((2, 5))

print('Original Array:', array)
print('Reshaped Array:\n', reshaped_array)
