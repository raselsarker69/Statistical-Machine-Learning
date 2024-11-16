import numpy as np

# Creating an array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Calculates statistical functions
mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)
variance_val = np.var(arr)

print('Mean:', mean_val)
print('Median:', median_val)
print('Standard Deviation:', std_val)
print('Variance:', variance_val)
