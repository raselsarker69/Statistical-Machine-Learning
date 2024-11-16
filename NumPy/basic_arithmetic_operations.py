import numpy as np

# Creating square matrices
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])


print("Matrix Summation:\n", matrix1 + matrix2, "\n")
print("Matrix Subtraction:\n", matrix1 - matrix2, "\n")
print("Matrix Element-wise Multiplication :\n", matrix1 * matrix2, "\n")
print("Matrix Element-wise Division :\n", matrix1 / matrix2, "\n")
print("Matrix Modulus :\n", matrix1 % matrix2, "\n")
print("Matrix Exponentiation:\n", matrix1 ** matrix2, "\n")
print("Matrix Floor Division:\n", matrix1 // matrix2, "\n")
