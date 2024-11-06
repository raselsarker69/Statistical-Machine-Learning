import numpy as np

# Creating a 3D array
array_3d = np.array([[[1, 2, 3, 4], 
                      [5, 6, 7, 8], 
                      [9, 10, 11, 12]]])

# Mixing slicing with direct indexing
#mixed_inx = array_3d[0, 0, 2]
mixed_inx = array_3d[1:, 0, 1]

print(mixed_inx)
