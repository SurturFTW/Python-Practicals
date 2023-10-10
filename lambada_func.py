from functools import reduce

# Sample list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter using a lambda function
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))

# Map using a lambda function
mapped_list = list(map(lambda x: x * 2, my_list))

# Reduce using a lambda function
reduced_result = reduce(lambda x, y: x + y, my_list)

# Print the results
print("Original List:", my_list)
print("Filtered List (even numbers):", filtered_list)
print("Mapped List (doubled values):", mapped_list)
print("Reduced Result (sum of all elements):", reduced_result)
