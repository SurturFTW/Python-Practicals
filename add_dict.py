# Define two dictionaries
dict1 = {'a': 12, 'b': 59, 'c': 71}
dict2 = {'b': 13, 'c': 22, 'd': 101}

# Concatenate the two dictionaries
concatenated_dict = {**dict1, **dict2}

# Calculate the sum of all values in the concatenated dictionary
total_sum = sum(concatenated_dict.values())

# Display the concatenated dictionary and the sum
print("Concatenated Dictionary:")
print(concatenated_dict)
print(f"Sum of all values: {total_sum}")