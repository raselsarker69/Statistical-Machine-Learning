# Using shift() for Time Series Analysis
import pandas as pd

# Creating a time series DataFrame
date_range = pd.date_range(start='2023-01-01', periods=5, freq='D')
data = {'Sales': [200, 250, 300, 350, 400]}
df = pd.DataFrame(data, index=date_range)

# Shifting the data to create a lag
df['Previous Day Sales'] = df['Sales'].shift(1)

print('DataFrame with Shifted Time Series Data:\n', df)