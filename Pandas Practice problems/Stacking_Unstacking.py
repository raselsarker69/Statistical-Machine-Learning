# Stacking and Unstacking DataFrames
### Stacking : Stacking converts columns into row levels, useful for hierarchical or grouped data representation.
### Unstacking : Unstacking reverts row levels back into columns, useful for a wider data representation.

    
import pandas as pd

# Creating a DataFrame
data = {'City': ['California', 'Florida'], '2020': [100, 150], '2021': [200, 250]}
df = pd.DataFrame(data).set_index('City')

# Stacking and unstacking the DataFrame
stacked_df = df.stack()
unstacked_df = stacked_df.unstack()

print('Stacked DataFrame:\n', stacked_df)
print('Unstacked DataFrame:\n', unstacked_df)