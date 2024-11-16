# Using applymap for Element-wise Operations
import pandas as pd

# Creating a DataFrame
data = {
    'A': [1, 2, 3], 
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)

# Applying various operations and storing results separately
df_squared = df.applymap(lambda x: x**2)
df_doubled = df.applymap(lambda x: x*2)
df_added_2 = df.applymap(lambda x: x+2)
df_subtracted_2 = df.applymap(lambda x: x-2)
df_floored_div_2 = df.applymap(lambda x: x//2)
df_mod_2 = df.applymap(lambda x: x%2)

# Printing results
print('DataFrame with Squared Values:\n', df_squared)
print('\nDataFrame with Doubled Values:\n', df_doubled)
print('\nDataFrame with Values Increased by 2:\n', df_added_2)
print('\nDataFrame with Values Decreased by 2:\n', df_subtracted_2)
print('\nDataFrame with Floored Division by 2:\n', df_floored_div_2)
print('\nDataFrame with Modulus 2:\n', df_mod_2)
