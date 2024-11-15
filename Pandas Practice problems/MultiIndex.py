# Example 2: Pandas - MultiIndex DataFrame Operations
import pandas as pd

# Creating a MultiIndex DataFrame
arrays = [['A', 'A', 'B', 'B'], 
          [2020, 2021, 2020, 2021]]

index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'Year'))
data = [100, 150, 200, 250]
df = pd.DataFrame(data, index=index, columns=['Sales'])

# Accessing data in a MultiIndex DataFrame
sales_in_2020 = df.xs(2020, level='Year')
sales_in_2021 = df.xs(2021, level='Year')

print('Sales Data in 2020:\n', sales_in_2020)
print('=================================:\n')
print('Sales Data in 2021:\n', sales_in_2021)