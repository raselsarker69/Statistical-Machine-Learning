import numpy as np

# Creating two arrays with different shapes
x = np.array([[1], [2], [3]]) 
y = np.array([4, 5, 6])      


result = x + y  # This uses broadcasting automatically
print("Result of broadcasting x + y:\n", result)

b = np.broadcast(x, y)
print("Broadcast shape:", b.shape)

