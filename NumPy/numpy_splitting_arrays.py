import numpy as np

# Creating an array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

split_arr = np.array_split(arr, 2)   # two parts
split_arr2 = np.array_split(arr, 3)   # three parts

print(f"Spliting the array is:\n", split_arr)
print(f"Spliting the array is:\n", split_arr2)