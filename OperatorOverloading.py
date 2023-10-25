class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, Vector):
            # Add the x and y components of two vectors and return a new Vector
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +: " + type(other).__name__)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Create two Vector instances
v1 = Vector(1, 2)
v2 = Vector(3, 4)
# Use the overloaded + operator
result = v1 + v2
print(result) # Output: (4, 6)
