# advanced slicing with step

import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix[:2])   # first two rows (0 and 1)
print(matrix[1:2])  # second row (row index 1)
print(matrix[2:2])  # Empty slice (start and end indices are the same)
print(matrix[3:])   # Out of bounds, returns an empty array
print(matrix[:])    # Prints all elements in the matrix

