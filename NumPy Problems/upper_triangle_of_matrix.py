# Extracting Upper Triangle of a Matrix
import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

uper_traingle = np.triu(matrix)
print(uper_traingle)