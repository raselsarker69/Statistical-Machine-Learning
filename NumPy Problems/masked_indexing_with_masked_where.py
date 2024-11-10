# Masked Indexing with np.ma.masked_where
import numpy as np

# Creating an array
array = np.array([1, -2, 3, -4, 5])

# Masking elements where values are negative
masked_array = np.ma.masked_where(array < 0, array)
print('Masked Array with Negative Values Hidden:', masked_array)

#Only Positive Values
array = np.array([1, -2, 3, -4, 5])
positive_array = array[array >= 0]
print('Array with Only Positive Values:', positive_array)


# Zero replace by NAN Value 
array = np.array([1, -2, 3, -4, 5])
masked_array = np.where(array < 0, np.nan, array)
print('Array with NaN for Negative Values:', masked_array)

#Negative Values Clipped to Zero
array = np.array([1, -2, 3, -4, 5])
clipped_array = np.clip(array, 0, None)
print('Array with Negative Values Clipped to Zero:', clipped_array)
