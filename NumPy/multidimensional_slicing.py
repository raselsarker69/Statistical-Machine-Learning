# NumPy - Multi-dimensional Slicing
import numpy as np

# Creating a 2D array
array_2d = np.array([[1, 2, 3, 4], 
                     [5, 6, 7, 8], 
                     [9, 10, 11, 12]])

# Multi-dimensional slicing
# Slice 1: Select rows starting from index 1 and columns 1 to 3 (up to, but not including, 4)
sub_array = array_2d[1:, 1:4]

# Slice 2: Select rows starting from index 1 and only the first two columns
slice_array = array_2d[1:, :2]

# Printing the results
print("Original Array:\n", array_2d)
print("\nSub Array (Rows 1 to end, Columns 1 to 3):\n", sub_array)
print("\nSlice Array (Rows 1 to end, Columns 0 and 1):\n", slice_array)
