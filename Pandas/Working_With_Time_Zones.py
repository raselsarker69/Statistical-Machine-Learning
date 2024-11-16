# Pandas - Working with Time Zones
import pandas as pd

# Creating a time series with a timezone (UTC)
date_range = pd.date_range(start='2023-01-01', periods=10, freq='D', tz='UTC')
data = {'Sales': [100, 200, 150, 300, 250, 120, 220, 180, 260, 280]}
df = pd.DataFrame(data, index=date_range)

# Converting to different timezones
df_us_eastern = df.tz_convert('US/Eastern')
print("DataFrame converted to US/Eastern timezone:\n", df_us_eastern)

df_london = df_us_eastern.tz_convert('Europe/London')
print("\nDataFrame converted to Europe/London timezone:\n", df_london)

# Removing the timezone
df_no_timezone = df_london.tz_localize(None)
print("\nDataFrame with timezone removed:\n", df_no_timezone)
