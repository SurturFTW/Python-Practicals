# Parent class 1
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

# Parent class 2
class Flyable:
    def fly(self):
        pass

# Parent class 3
class Swimmable:
    def swim(self):
        pass

# Child class inheriting from Animal and Flyable
class Bird(Animal, Flyable):
    def speak(self):
        return f"{self.name} says Tweet!"
    def fly(self):
        return f"{self.name} is flying."

# Child class inheriting from Animal and Swimmable
class Fish(Animal, Swimmable):
    def speak(self):
        return f"{self.name} says Blub!"
    def swim(self):
        return f"{self.name} is swimming."


# Child class inheriting from Bird and Fish
class Duck(Bird, Fish):
    def __init__(self, name):
        super().__init__(name)

# Create instances of Duck and demonstrate multiple inheritance
donald = Duck("Donald")
print(donald.speak())
print(donald.fly())
print(donald.swim())
