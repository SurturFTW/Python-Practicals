try:
    # Code that may raise exceptions
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    result = num1 / num2
    print(f"Result: {result}")

except ValueError:
    # Handle the ValueError exception (e.g., if user inputs a non-integer)
    print("Please enter valid integer values.")

except ZeroDivisionError:
    # Handle the ZeroDivisionError exception (e.g., if the second number is 0)
    print("Cannot divide by zero.")

except Exception as e:
    # Catch all other exceptions
    print(f"An error occurred: {e}")

finally:
    # This block is optional, and it will execute whether there's an exception or not.
    print("Execution completed.")
    # Rest of the program continues here...
    print("Program continues...")
