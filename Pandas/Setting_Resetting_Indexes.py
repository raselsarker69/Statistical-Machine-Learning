# Setting and Resetting Indexes
import pandas as pd

# Creating a DataFrame
data = {
    'City': ['Dhaka', 'Rangpur', 'Sylet'], 
    'Year': [2020, 2021, 2021], 
    'Sales': [100, 200, 300]
}
df = pd.DataFrame(data)

# Setting an index
df.set_index('City', inplace=True)
print('DataFrame after Setting Index:\n', df)

# Changing column names
df.rename(columns={'Year': 'Year_of_Sale', 'Sales': 'Total_Sales'}, inplace=True)
df.index.name = 'Location'  # Renaming the index name

print('\nDataFrame after Renaming Columns and Index Name:\n', df)

# Resetting the index
df.reset_index(inplace=True)

# Changing column names back if necessary
df.rename(columns={'Location': 'City', 'Year_of_Sale': 'Year', 'Total_Sales': 'Sales'}, inplace=True)

print('\nDataFrame after Resetting Index and Reverting Names:\n', df)
