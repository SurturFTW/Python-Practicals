import pandas as pd

# Sample data for two DataFrames
data1 = {'ID': [1, 2, 3], 'Name': ['Prasad', 'Anish', 'Shreya']}
data2 = {'ID': [2, 3, 4], 'Age': [25, 30, 35]}

# Create the first DataFrame
df1 = pd.DataFrame(data1)

# Create the second DataFrame
df2 = pd.DataFrame(data2)

# Merge the two DataFrames on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='inner')

# Display the merged DataFrame
print(merged_df)
