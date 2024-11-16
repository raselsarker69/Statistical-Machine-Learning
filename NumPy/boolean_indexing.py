# Boolean indexing and slicing
import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


print(f"Grether then 6:\n", matrix[matrix > 6])

print("Greater than 5:\n", matrix[matrix > 5])

print("Less than or equal to 4:\n", matrix[matrix <= 4])

matrix[matrix > 5] = 0
print("Matrix after replacing elements > 5 with 0:\n", matrix)

matrix[matrix % 2 == 0] = -1  # Set all even numbers to -1
print("Matrix after setting even numbers to -1:\n", matrix)

matrix[matrix % 2 != 0] = 33  # Set all even numbers to 33
print("Matrix after setting even numbers to -1:\n", matrix)