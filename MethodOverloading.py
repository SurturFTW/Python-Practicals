class MathOperations:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

    def multiply(self, a, b, c=None):
        if c is not None:
            return a * b * c
        else:
            return a * b

# Create an instance of the MathOperations class
math = MathOperations()

# Call the overloaded methods
result1 = math.add(2, 3)
result2 = math.add(2, 3, 4)
result3 = math.multiply(2, 3)
result4 = math.multiply(2, 3, 4)
print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
print("Result 4:", result4)
