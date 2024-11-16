# advanced indixing with meshgrid
# The meshgrid function returns two 2-dimensional arrays 
import numpy as np

# Creating a square matrix
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr1 = np.linspace(-4, 4, 11)
arr2 = np.linspace(-5, 5, 22)

ar1, ar2 = np.meshgrid(arr1, arr2)

print(f"Array ar1:\n{ar1}")
print(f"Array ar2:\n{ar2}")
