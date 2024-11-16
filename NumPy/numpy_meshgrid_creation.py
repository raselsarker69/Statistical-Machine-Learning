# Meshgrid Creation
import numpy as np

# Creating 1D arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Creating a meshgrid
X, Y = np.meshgrid(x, y)
X, Y = np.meshgrid(x, y, indexing='ij')
Z = np.sin(np.sqrt(X**2 + Y**2))

x = np.array([1, 2])
y = np.array([3, 4])
z = np.array([5, 6])

X, Y, Z = np.meshgrid(x, y, z)

print("X:\n", X)
print("Y:\n", Y)
print("Z:\n", Z)


print('Meshgrid X:\n', X)
print('Meshgrid Y:\n', Y)

print("X:\n", X)
print("Y:\n", Y)
print("Z:\n", z)