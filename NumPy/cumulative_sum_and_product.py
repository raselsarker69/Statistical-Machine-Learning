# Cumulative Sum and Product
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4])

# Calculating cumulative sum and product
cumulative_sum = np.cumsum(array)
cumulative_product = np.cumprod(array)

print('Cumulative Sum:', cumulative_sum)
print('Cumulative Product:', cumulative_product)

############# Explain sum and products
# Calculating the Cumulative sum
# For this array [1, 2, 3, 4]:
# First element: 1
# Second element: 1 + 2 = 3
# Third element: 1 + 2 + 3 = 6
# Fourth element: 1 + 2 + 3 + 4 = 10

# # Calculating the Cumulative Product
# For this array [1, 2, 3, 4]:
# First element: 1
# Second element: 1 * 2 = 2
# Third element: 1 * 2 * 3 = 6
# Fourth element: 1 * 2 * 3 * 4 = 24