nested_list = [[10, 20, 30], [40, 50, [60, 70]], [80, 90]]

# Accessing a nested element
nested_element = nested_list[1][2][0]  # Accessing 60

# Modifying nested element
nested_list[2][1] = 100  # Changing 90 to 100

# Flattening the nested list
flattened_list = [element for sublist in nested_list for item in sublist for element in (item if isinstance(item, list) else [item])]

print('Nested Element:', nested_element)
print('Modified Nested List:', nested_list)
print('Flattened List:', flattened_list)
