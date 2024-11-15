import pandas as pd

# Corrected sample data with consistent lengths for all columns
data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-02'],
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Department': ['CSE', 'EEE', 'IPE', 'ME', 'BME', 'ANN'],
    'Subject': ['Math', 'History', 'Physics', 'Literature', 'Chemistry', 'Philosophy'],
    'Score': [85, 90, 78, 88, 92, 75]
}


df = pd.DataFrame(data)

# Pivoting to create a DataFrame with MultiIndex columns
pivot_df = df.pivot(
    index='Date', 
    columns=['Student', 'Department', 'Subject'],  # Multiple index columns
    values='Score'
)

print('Pivoted DataFrame with MultiIndex Columns:\n', pivot_df)



