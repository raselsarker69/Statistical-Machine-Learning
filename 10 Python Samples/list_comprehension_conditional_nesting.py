matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

# Filtering even numbers from the matrix
even_numbers = [num for row in matrix for num in row if num % 2 == 0]
odd_numbers = [num for row in matrix for num in row if num % 2 != 0]

print('Even Numbers:', even_numbers)
print('Odd Numbers:', odd_numbers)
