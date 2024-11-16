# Renaming Index and Columns
import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Rasel', 'sarker'],
    'Dept': ['CSE', 'EEE'],
    'Score': [100, 200]
}
df = pd.DataFrame(data, index=['Row1', 'Row2'])

# Renaming index and columns
df_renamed = df.rename(index={'Row1': 'Student1', 'Row2': 'Student2'}, columns={'Score': 'Grade'})
print('Original DataFrame:\n', df)
print("================================\n")
print('Renamed DataFrame:\n', df_renamed)