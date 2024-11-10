# Combining multiple indexing.

import numpy as np

# Creating a 2D array 
array = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]
])

# 1. Using Integer Indexing and Slicing Together
sub_array1 = array[1:3, [1, 3]]  # Select rows 1 and 2, and columns 1 and 3
print("Sub-array 1 (Integer Indexing and Slicing):")
print(sub_array1)

# 2. Using Boolean Indexing and Integer Indexing Together
result = array > 100
sub_array2 = array[result]  # Elements greater than 100
print("\nSub-array 2 (Boolean Indexing):")
print(sub_array2)


filtered_idx = [1, 3, 5]  # Select specific idx after flattening
print("\nFiltered Elements by specific idx:")
print(sub_array2[filtered_idx])


# Retrieve all rows but only the columns where values in the first row are greater than 20
sub_array3 = array[:, array[0, :] > 20]
print("\nSub-array 3 (Slicing and Boolean Indexing):")
print(sub_array3)
