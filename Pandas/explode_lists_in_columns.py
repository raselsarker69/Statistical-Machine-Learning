# Using Explode for Lists in Columns
import pandas as pd

# Creating a DataFrame with lists in a column
data = {
    'ID': [1, 2], 
    'Hobbies': [['Reading', 'Swimming'], ['Running', 'Cycling']]
}
df = pd.DataFrame(data)

# Exploding the 'Hobbies' column
exploded_df = df.explode('Hobbies')

# Printing the result
print('DataFrame after Exploding Lists:\n', exploded_df)
