import pandas as pd

# Correcting data structure and format
data = {
    'Name': ['Rasel', 'Rahim', 'Rakib', 'Ramisha', 'Arman'],
    'Dept': ['CSE', 'ML', 'ME', 'IPE', 'EEE']
}
df = pd.DataFrame(data)

# Mapping departments to EINN
department_map = {'CSE': 2000, 'ML': 2005, 'ME': 2009, 'IPE': 2010, 'EEE': 1998}
df['Dept EINN'] = df['Dept'].map(department_map)

print(df)