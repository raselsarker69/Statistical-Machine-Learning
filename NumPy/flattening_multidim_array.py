# Flattening a Multi-dimensional Array
# Flattening thats means converts 2D array to 1D array
import numpy as np

# Creating a 2D array
array_2d = np.array([[10, 20, 30], 
                     [40, 50, 60], 
                     [70, 80, 90]])

# Flattening the array
flattened_array = array_2d.flatten()

print('Flattened Array:', flattened_array)