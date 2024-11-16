# Power and squre root.

import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

pow_matrix = matrix * 2
sqr_matrix = matrix ** 2

print(f"Original Matrix:\n", matrix)
print(f"Power Matrix:\n", pow_matrix)
print(f"Square Matrix:\n",sqr_matrix)