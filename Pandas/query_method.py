# Query Method for Conditional Filtering
import pandas as pd

data = {
    'Name': ['Rasel', 'sarker'],
    'Dept': ['CSE', 'EEE'],
    'Score': [100, 200]
}

df = pd.DataFrame(data)

# Using query() with variables
filter_val = df.query('Score > 80')
print('Filtered DataFrame with query() and Variables:\n', filter_val)