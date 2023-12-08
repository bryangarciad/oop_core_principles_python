# Polymorphism in Object-Oriented Programming (OOP) refers to the ability of different classes to be treated as objects 
# of a common superclass through a shared interface. 
# This allows objects of different classes to be used interchangeably based on a common behavior or interface, 
# even though each class might have its own specific implementation.

class Vehicle:
    def print_details(self):
        return "Parent method from Vehicle class"

class Car(Vehicle):
    #Parent method overloading
    def print_details(self):
        return "Daughter method from Car class"

class Cycle(Vehicle):
    #Parent method overloading
    def print_details(self):
        return "Daughter method from Cycle class"

car1 = Vehicle()
car2 = Car()
car3 = Cycle()

print(car1.print_details())
print(car2.print_details())
print(car3.print_details())


#Parametric Polymorphism (Overloading): This refers to the ability to define multiple methods with the same name but different parameters or arguments.
#In your code, there's method overriding rather than overloading. 
#Overloading specifically involves methods in the same class having the same name but different parameters. An example could be:

#NOTE: Overloading is not supported in Python directly
class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

math = MathOperations()
print(math.add(2, 3))

#Ad hoc Polymorphism (Compile-time):
#Python does not directly support compile-time polymorphism; however, it uses duck typing to achieve similar behavior. 
#Duck typing allows different types to be used interchangeably based on their behavior rather than their type.

class Duck:
    def fly(self):
        return "Duck flying"

class Airplane:
    def fly(self):
        return "Airplane flying"

def lift_off(entity): #Note that a separate method is used as a facade to access the fly property for different classes that share behaviour
    return entity.fly()

duck = Duck()
airplane = Airplane()

print(lift_off(duck))    
print(lift_off(airplane)) 

