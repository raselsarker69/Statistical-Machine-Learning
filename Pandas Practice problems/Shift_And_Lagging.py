# Shift and Lagging Data
import pandas as pd

# Creating a DataFrame
data = {'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
        'Temperature': [30, 32, 35, 33, 31]}
df = pd.DataFrame(data)

# Shifting data by one day to create a lag
df['Prev Day Temp'] = df['Temperature'].shift(1)

print('DataFrame with Shifted Data:\n', df)