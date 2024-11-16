# 3D Array Indexing
import numpy as np

# Creating a 3D array
array_3d = np.array([[[10, 20, 30], 
                      [40, 50, 60]], 
                     
                     [[70, 80, 90], 
                      [100, 110, 120]]])

# Accessing elements in a 3D array
element = array_3d[1, 0, 1]  # Accessing the element at [1, 0, 1]

# Slicing in 3D
slice_3d = array_3d[:, 0, :]

print('Element at (1,0,1):', element)
print('Sliced 3D Array:\n', slice_3d)