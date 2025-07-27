# Base class
class Animal:
    def __init__(self):
        print("Animal is initialized")
        self.type = "Wild Animal"

    def sound(self):
        print("Animals make sound")

# Derived class
class Dog(Animal):
    def __init__(self):
        # Call the constructor of the parent class using super()
        super().__init__()
        print("Dog is initialized")
        self.breed = "Labrador"

    def sound(self):
        # Call the sound() method of the parent class
        super().sound()
        print("Dog barks")

# Create an instance of Dog
d = Dog()

# Call the overridden method
d.sound()
