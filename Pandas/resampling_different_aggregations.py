# ***Resampling***: Changing the frequency of the time series data, such as converting hourly data to daily, daily to weekly, etc.
# ***Different Aggregations***: Applying various functions to summarize the data within each new interval. (min/max, median, sum, std)

# Resampling with Different Aggregations
import pandas as pd

# Creating a time series DataFrame
date_range = pd.date_range(start='2024-01-01', periods=50, freq='D')
data = {'Sales': range(50)}
df = pd.DataFrame(data, index=date_range)

# Resampling with different aggregations
resampled_df = df.resample('W').agg({
    'Sales': ['sum', 'mean', 'max', 'median']
})

print('Resampled DataFrame with Different Aggregations:\n', resampled_df)

