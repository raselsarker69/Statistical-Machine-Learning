# Python Lambda
# A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.
# একটি ল্যাম্বডা ফাংশন যেকোনো সংখ্যক আর্গুমেন্ট নিতে পারে, কিন্তু শুধুমাত্র একটি এক্সপ্রেশন থাকতে পারে। 
import pandas as pd 

data = {
    'Name': ['Rasel', 'sarker', 'sakib', 'Rafi'],
    'Dept': ['CSE', 'EEE', 'IPE', 'BME'],
    'Score': [60, 70, 80, 90]
}

df = pd.DataFrame(data)

df['Adjust score'] = df['Score'].apply(lambda x: x + 10 if x < 90 else x)

print('DataFrame with Adjusted Scores:\n', df)