# Setting and Resetting Indexes
# set_index and reset_index
import pandas as pd

# Creating a DataFrame
data = {
    'City': ['Dk', 'Ctg', 'Syt'], 
    'Year': [2020, 2021, 2021], 
    'Sales': [100, 200, 300]
}
df = pd.DataFrame(data)

# Setting an index
df_with_index = df.set_index('City')  # Setting 'City' as the index

# Resetting the index
df_reset_index = df_with_index.reset_index()  # Resetting the index back to default 0,1,2

print('DataFrame after Setting Index:\n', df_with_index)

print('====================================')

print('DataFrame after Resetting Index:\n', df_reset_index)
