import numpy as np

integer_array = np.random.randint(0, 100, size=10)  # Random integers between 0 and 100 with 10 elements
float_array = np.random.rand(10)                    # Array of random floats between 0 and 1
random_array = np.random.rand(3, 3)                 # Random float values in a 3x3 array
normal_array = np.random.randn(3, 3)                # Random values with a normal (Gaussian) distribution in 3x3 array


print("Random Integer Array:\n", integer_array)
print("Random Float Array:\n", float_array)
print("3x3 Random Float Array:\n", random_array)
print("3x3 Normal Distribution Array:\n", normal_array)
