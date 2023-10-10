# Convert Celsius to Fahrenheit using a lambda function
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32

# Temperature in Celsius
celsius_temperature = 25

# Use the lambda function to convert
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

# Print the result
print(celsius_temperature, "degrees Celsius is equal to ", fahrenheit_temperature , "degrees Fahrenheit.")
