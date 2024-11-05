import numpy as np

# Creating an array
arr = np.array([11, 2, 3, 40, 5, 6, 7, 8, 9, 10])

# Slicing the array in different ways
slicing_second = arr[::2]   # Every second element
slicing_third = arr[::3]    # Every third element
slicing_fourth = arr[::4]   # Every fourth element
slicing_from_second = arr[2::3]   # Start from the 3rd element, then every third element

print("Every second element:\n", slicing_second)
print("Every third element:\n", slicing_third)
print("Every fourth element:\n", slicing_fourth)
print("Every third element starting from the 3rd element:\n", slicing_from_second)

