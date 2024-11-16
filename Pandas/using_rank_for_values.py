# Using Rank to Rank Values
import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'], 
    'Score': [85, 90, 78, 92]
}
df = pd.DataFrame(data)

# Ranking scores in descending order
df['Grade'] = df['Score'].rank(ascending=False)

print('DataFrame with Ranked Scores:\n', df)