# Example 2: Tuple Unpacking
# Unpacking a tuple with multiple values into variables, including using the * operator for remaining values.

person_info = (
    'Rasel Sarker', 
    2001, 
    'Student', 
    'CSE', 
    'Mathematics',  # favorite subject
    'Reading', 'Gaming'  # hobbies
)

# Unpacking 
name, birth_year, occupation, department, favorite_subject, *hobbies = person_info

print('Name:', name)
print('Birth Year:', birth_year)
print('Occupation:', occupation)
print('Department:', department)
print('Favorite Subject:', favorite_subject)
print('Hobbies:', hobbies)




