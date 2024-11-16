# Rank for values
import pandas as pd

# Correcting data structure and format
data = {
    'Name': ['Rasel', 'Rahim', 'Rakib', 'Ramisha'],
    'Score': [20, 30, 40, 50]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Applying rank to the 'score' column
#df['Rank'] = df['Score'].rank(ascending=False)
df['Rank'] = df['Score'].rank(ascending=True)

print(df)
