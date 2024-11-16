
import pandas as pd

# Creating a date range for 10 days starting from January 1, 2023
date_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = {
    'Sales': [120, 135, 150, 180, 160, 210, 195, 225, 215, 230]
}

df = pd.DataFrame(data, index=date_range)

# Resampling data for daily, weekly, and monthly sales
daily_sales = df.resample('D').sum()
weekly_sales = df.resample('W').sum()
monthly_sales = df.resample('M').sum()

print('Original Sales:\n', df)
print('\nDaily Sales:\n', daily_sales)
print('\nWeekly Sales:\n', weekly_sales)
print('\nMonthly Sales:\n', monthly_sales)

