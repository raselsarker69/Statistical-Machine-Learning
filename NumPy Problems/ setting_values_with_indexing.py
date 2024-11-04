import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# Setting a value with index
matrix[1, 2] = 10  # Changing the element at row 1, column 2 to 10
matrix[2, 2] = 100
matrix[0, 2] = 33

print(matrix)
print(matrix[1])