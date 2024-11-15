# Using pivot_table with Multiple Indexes
# Using a pivot table with multiple indexes in pandas allows you to create a summary table by grouping data on more than one key (or index).

import pandas as pd

# Creating a DataFrame
data = {
    'City': ['Dhaka', 'Rangpur', 'Cittagong', 'Sylet', 'Gaibandha'], 
    'Year': [2020, 2020, 2021, 2021, 2020], 
    'Sales': [100, 150, 200, 250, 300]
}
df = pd.DataFrame(data)

# Creating a pivot table with multiple indexes
pivot_table = pd.pivot_table(df, values='Sales', index=['City', 'Year'], aggfunc='sum')

# Aggregating by City, calculating the sum of Sales in each city
result = df.groupby('City').agg({'Sales': 'sum'})


print("Aggregated Sales by Region:\n", result)
print("=======================================:\n")
print('Pivot Table with Multiple Indexes:\n', pivot_table)