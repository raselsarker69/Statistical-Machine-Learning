# Conditional index
import numpy as np

# Creating an array
array = np.array([10, 15, 20, 25, 30])

# j idx ar value 20 ar choto or equl i will print this value.
for i in array:
    if i > 20:
        break
    print(i)

