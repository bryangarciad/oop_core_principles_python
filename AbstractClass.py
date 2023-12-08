# Abstraction in object-oriented programming (OOP) is the concept of hiding the complex implementation details 
# and showing only the necessary features of an object. It allows you to focus on what an object does rather than how it does it.

from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

# Concrete classes inheriting from Shape
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def area(self):
        return self.side * self.side

# Using the classes
circle = Circle("Circle", 5)
square = Square("Square", 4)

print(circle.area())  # Output: 78.5
print(square.area())  # Output: 16
