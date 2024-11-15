# Using query() with Variables
# # Using the `@` symbol to reference external variables in query

import pandas as pd

data = {
    'Name': ['Rasel', 'sarker'],
    'Dept': ['CSE', 'EEE'],
    'Score': [100, 200]
}

df = pd.DataFrame(data)

# Using query() with variables
val = 50
filter_val = df.query('Score > @val')
print('Filtered DataFrame with query() and Variables:\n', filter_val)