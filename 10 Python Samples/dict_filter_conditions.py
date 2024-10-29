# Example 9: Dictionary Filtering Based on Conditions

dict1 = {
    'Rasel': 100,
    'Rahim': 200,
    'Rafiya': 300,
    'David': 55,
}

filtered_scores = {name: dict1 for name, dict1 in dict1.items() if dict1 >= 100}
print('Filtered Scores:', filtered_scores)