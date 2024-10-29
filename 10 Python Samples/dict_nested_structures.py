# Accessing and modifying elements in a dictionary with nested structures.

nested_dict = {
    'person': {
        'name': 'Rasel Sarker',
        'details': {
            'age': 24,
            'city': 'Gaibandha',
            'skills': ['Python', 'Data Science', 'Machine Learning', 'Deep Learning']
        }
    }
}

# Accessing nested elements
print("Name:", nested_dict['person']['name'])
print("City:", nested_dict['person']['details']['city'])
print("Skills:", nested_dict['person']['details']['skills'])

# Modifying a nested element
nested_dict['person']['details']['city'] = 'Dhaka'

# Adding new skill
nested_dict['person']['details']['skills'].append('Deep Learning')

print("\nUpdated Nested Dictionary:", nested_dict)
