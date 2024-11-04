# Basic indexing and slicing
import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Row 1:", matrix[1])         
print("Row 2:", matrix[2])        
matrix[1, 2] = 10                  
print("Updated Matrix:\n", matrix) 

print("First two rows:\n", matrix[:2])      
print("Second row:\n", matrix[1:2])        
print("Third row:\n", matrix[2:3])          
print("Entire matrix:\n", matrix[:])        
print("Empty slice (2:2):\n", matrix[2:2])   


