# Creating Dummy Variables
import pandas as pd

# Creating a DataFrame
data = {'City': ['NY', 'LA', 'SF', 'NY']}
df = pd.DataFrame(data)

# Creating dummy variables
dummies = pd.get_dummies(df['City'], prefix='City')

print('Dummy Variables DataFrame:\n', dummies)