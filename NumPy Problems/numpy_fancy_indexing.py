# Fancy Indexing
# Fancy indexing allows flexible and complex selections of array elements using arrays of indices, 
# which can be highly useful for selecting, filtering, or reordering data efficiently.

import numpy as np

# Creating a 2D array
data = np.array([[100, 200, 300],
                 [400, 500, 600],
                 [700, 800, 900]])

# Select elements in a fancy way
row_indices = [0, 1, 2]   
col_indices = [2, 1, 0]
result = data[row_indices, col_indices]

print("Fancy Indexed Elements:", result) 

# row_indices[0] and col_indices[0] point to row 0, column 2.
# row_indices[1] and col_indices[1] point to row 1, column 1.
# row_indices[2] and col_indices[2] point to row 2, column 0.