import numpy as np

# Creating an array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

reverse_arr = np.sort(arr)[::-1]

print("Reversed Array in Descending Order:\n", reverse_arr)
print("Third element of the Reversed array:", reverse_arr[2])


