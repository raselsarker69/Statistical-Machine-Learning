# Pandas - Cumulative Sum and Product
import pandas as pd

# Creating a DataFrame
data = {'Sales': [100, 200, 150, 300, 250]}
df = pd.DataFrame(data)

# Calculating cumulative sum and product
df['Cumulative Sum'] = df['Sales'].cumsum()
df['Cumulative Product'] = df['Sales'].cumprod()

print('DataFrame with Cumulative Operations:\n', df)