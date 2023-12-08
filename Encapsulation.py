# Encapsulation in Object-Oriented Programming (OOP) is a fundamental principle that involves bundling 
# the data (attributes) and methods (functions) that operate on the data within a single unit, known 
# as a class. 
# It helps in controlling the access to the inner workings of an object, 
# providing a way to protect its integrity and prevent unauthorized access.

class Car:
    def __init__(self, make, model, year):
        self._make = make  # Protected attribute
        self._model = model  # Protected attribute
        self.__year = year  # Private attribute

    def display_details(self):
        return f"Car: {self._make} {self._model} ({self.__year})"

    def update_year(self, new_year):
        self.__year = new_year  # Method to update private attribute


# Creating a Car object
my_car = Car("Toyota", "Corolla", 2020)

# Accessing attributes (public and protected)
print(my_car._make)  # Accessing protected attribute
# Output: Toyota

# Trying to access private attribute directly (won't work due to name mangling)
# print(my_car.__year)  # This will cause an AttributeError

# Accessing private attribute using name mangling (not recommended)
print(my_car._Car__year)  # Name mangling to access private attribute
# Output: 2020

# Using methods to access and modify private attribute
print(my_car.display_details())  # Output: Car: Toyota Corolla (2020)
my_car.update_year(2022)
print(my_car.display_details())  # Output: Car: Toyota Corolla (2022)
