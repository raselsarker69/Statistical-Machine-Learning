# Sorting by Multiple Columns
import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Rasel', 'Rahim', 'Rakib', 'Ramisha'],
    'Dept': ['CSE', 'EEE', 'IPE', 'ME'],
    'Score': [70, 50, 90, 100],
    'Age': [25, 30, 35, 22], 
}

df = pd.DataFrame(data)

# Sorting by multiple columns
sorted_df = df.sort_values(by=['Score', 'Age'], ascending=[False, True])

print('Sorted DataFrame by Multiple Columns:\n', sorted_df)