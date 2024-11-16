# Using style for DataFrame Styling
import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Rasel', 'Rahim', 'Rakib', 'Ramisha'],
    'Score': [70, 50, 90, 100]
}

df = pd.DataFrame(data)

# Applying styles to highlight scores above 80
styled_df = df.style.applymap(lambda x: 'background-color: yellow' if isinstance(x, int) and x > 80 else '')

# Display the styled DataFrame (use .render() if exporting to HTML)
print('Styled DataFrame with Conditional Formatting', styled_df)