# Creating a Pivot Table with Multiple Aggregations
import pandas as pd

# Sample data
data = {
    'City': ['Dhaka', 'Sylet', 'Rangpur', 'Bogura', 'Gaibandha', 'Ctg'],
    'Dpt': ['Electronics', 'Furniture', 'Electronics', 'Furniture', 'Electronics', 'Furniture'],
    'Product': ['TV', 'Sofa', 'TV', 'Sofa', 'TV', 'Sofa'],
    'Sales': [200, 150, 300, 100, 250, 120]
}

df = pd.DataFrame(data)

# Creating a pivot table with multiple indexes (City, Department, and Product) and multiple aggregations
pivot_table = df.pivot_table(
    values='Sales',
    index=['City', 'Dpt', 'Product'],  # Multiple indexe
    aggfunc=['sum', 'mean', 'std']     # Multiple aggregation
)

print("Pivot Table with Multiple Indexes and Aggregations:\n", pivot_table)
