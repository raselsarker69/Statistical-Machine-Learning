# NumPy broadcasting is a technique that allows NumPy to perform arithmetic operations on arrays of 
# different shapes in an efficient way without explicitly copying data. 
# Broadcasting rules apply when:
# 1) The dimensions are equal or
# 2) One of the dimensions is 1, allowing it to be "stretched" to match the other array.

import numpy as np

# Creating two arrays with different shapes
x = np.array([[1], [2], [3]]) 
y = np.array([4, 5, 6])      


result = x + y  # This uses broadcasting automatically
print("Result of broadcasting x + y:\n", result)

b = np.broadcast(x, y)
print("Broadcast shape:", b.shape)

