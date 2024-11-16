# Pandas - Merging on Multiple Columns
import pandas as pd

# Creating two DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Year': [2020, 2021, 2021], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 1], 'Year': [2021, 2021, 2020], 'Score': [88, 92, 75]})

# Merging on multiple columns
merged_df = pd.merge(df1, df2, on=['ID', 'Year'], how='inner')

print('Merged DataFrame on Multiple Columns:\n', merged_df)