import pandas as pd

# Sample data for two DataFrames
data1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
data2 = {'A': [7, 8, 9], 'B': [10, 11, 12]}

# Create the first DataFrame
df1 = pd.DataFrame(data1)

# Create the second DataFrame
df2 = pd.DataFrame(data2)

# Concatenate the two DataFrames along rows and assign all data
result = pd.concat([df1, df2])

# Display the aggregated DataFrame
print(result)
