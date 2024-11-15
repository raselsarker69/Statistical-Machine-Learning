import pandas as pd 

data = {
    'Name': ['Rasel', 'sarker', 'sakib', 'Rafi'],
    'Dept': ['CSE', 'EEE', 'IPE', 'BME'],
    'Score': [100, 200, 300, 400]
}

df = pd.DataFrame(data)

group_by = df.groupby('Name').agg({'Score': ['sum', 'mean']})
print(group_by)